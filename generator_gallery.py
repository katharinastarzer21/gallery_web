import os
import re
from pathlib import Path
from typing import List, Optional

import yaml
import nbformat

MYST_YML = "myst.yml"  # ggf. anpassen

# ------------------ Frontmatter-Reader ------------------

FRONTMATTER_RE = re.compile(r"^\s*---\s*\n(.*?)\n---\s*(?:\n|$)", re.DOTALL)

def read_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

def extract_yaml_from_markdown(md_path: Path) -> Optional[dict]:
    text = md_path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return None

def extract_yaml_from_notebook(nb_path: Path) -> Optional[dict]:
    with nb_path.open("r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
    for cell in nb.cells:
        if cell.cell_type == "markdown":
            content = (cell.source or "").strip()
            if content.startswith("---") and content.count("---") >= 2:
                _, yaml_block, _ = content.split("---", 2)
                try:
                    return yaml.safe_load(yaml_block) or {}
                except yaml.YAMLError:
                    return None
            break
    return None

def load_meta(path: Path) -> dict:
    if path.suffix.lower() == ".ipynb":
        return extract_yaml_from_notebook(path) or {}
    if path.suffix.lower() in {".md", ".markdown", ".mdx"}:
        return extract_yaml_from_markdown(path) or {}
    return {}

# ------------------ Rendering ------------------

def normalize_thumbnail(thumb: str, gallery_dir: Path) -> str:
    thumb = (thumb or "").strip()
    if not thumb:
        return ""
    if thumb.startswith(("http://", "https://")):
        return thumb
    if "img/" in thumb:
        rel = thumb.split("img/", 1)[1].lstrip("/")
        return f"../img/{rel}"
    return thumb

def generate_card(meta: dict, link_href: str, thumbnail_href: str) -> str:
    title = meta.get("title", "Untitled")
    subtitle = meta.get("subtitle") or meta.get("description") or "no description"
    tags = meta.get("tags", [])
    tags_html = "".join(
        f'<span class="tag" style="display:inline-block;margin-right:6px;padding:2px 8px;'
        f'border:1px solid #ccd9ea;border-radius:999px;font-size:12px;">{t}</span>'
        for t in tags
    )
    return f"""
<div class="notebook-card" data-tags="{' '.join(tags)}" style="display:flex;align-items:flex-start;border:1px solid #cddff1;border-radius:6px;padding:14px 20px;background:#f9fbfe;box-shadow:1px 1px 4px #dfeaf5;">
  <div style="width:120px;height:90px;flex-shrink:0;display:flex;align-items:center;justify-content:center;background:#fff;border:1px solid #e0eaf5;border-radius:6px;overflow:hidden;margin-right:24px;">
    <img src="{thumbnail_href}" alt="Thumbnail" style="max-width:100%;max-height:100%;object-fit:contain;">
  </div>
  <div style="flex:1;">
    <strong>{title}</strong><br>
    <div style="margin:4px 0 8px 0;">{subtitle}</div>
    <div style="margin:6px 0 10px 0;">{tags_html}</div>
    <a href="{link_href}" style="text-decoration:none;color:#1d70b8;font-weight:bold;">View Notebook</a>
  </div>
</div>
""".strip()

def wrap_gallery(cards: List[str], title: str) -> str:
    return f"""# {title} Gallery

### Filter Notebooks by Tags
<div id="tag-filter" style="margin:10px 0 20px 0;">
  <input type="text" id="tagInput" placeholder="type tags…" 
         style="width:100%;max-width:420px;padding:8px;border:1px solid #cddff1;border-radius:6px;">
</div>

<div id="gallery" style="display:flex;flex-direction:column;gap:20px;max-width:900px;">
{os.linesep.join(cards)}
</div>

<script>
// simpler AND-Filter
const input = document.getElementById('tagInput');
const cards = Array.from(document.querySelectorAll('.notebook-card'));
input.addEventListener('input', () => {{
  const q = input.value.trim().toLowerCase().split(/\\s+/).filter(Boolean);
  cards.forEach(c => {{
    const tags = (c.getAttribute('data-tags') || '').toLowerCase().split(/\\s+/).filter(Boolean);
    const match = q.every(t => tags.includes(t));
    c.style.display = match ? 'flex' : 'none';
  }});
}});
</script>
""".rstrip()

# ------------------ Core ------------------

def build_gallery_for_service(service_title: str, service_file: str, hidden_files: List[str]) -> Path:
    """
    Nimmt ausschließlich die in 'hidden' gelisteten Dateien und erzeugt
    <service_name_lower>_gallery.md im selben Ordner wie 'service_file'.
    """
    service_page = Path(service_file)
    service_dir = service_page.parent if service_page.parent.as_posix() != "." else Path(".")
    service_name = service_title.lower().replace(" ", "_")
    gallery_file = service_dir / f"{service_name}_gallery.md"

    cards = []
    for hidden in hidden_files:
        p = Path(hidden)
        if not p.exists():
            print(f"[WARN] not found, skip: {p}")
            continue
        meta = load_meta(p)
        link = os.path.relpath(p, start=gallery_file.parent).replace("\\", "/")
        thumb = normalize_thumbnail(meta.get("thumbnail", ""), gallery_file.parent)
        cards.append(generate_card(meta, link, thumb))

    gallery_file.parent.mkdir(parents=True, exist_ok=True)
    gallery_file.write_text(wrap_gallery(cards, service_title), encoding="utf-8")
    print(f"[GALLERY] {gallery_file} -> {len(cards)} cards")
    return gallery_file

def main():
    myst = read_yaml(Path(MYST_YML))
    toc = myst.get("project", {}).get("toc", [])
    services = next((x for x in toc if isinstance(x, dict) and x.get("title") == "Services"), None)
    if not services:
        raise SystemExit("No 'Services' block found in myst.yml -> project.toc")

    for svc in services.get("children", []):
        if not isinstance(svc, dict):
            continue
        title = svc.get("title")
        file_ = svc.get("file")
        hidden = svc.get("hidden", [])
        if not title or not file_:
            continue
        # NUR hidden-Dateien hernehmen
        build_gallery_for_service(title, file_, hidden)

if __name__ == "__main__":
    main()
