import os
import re
import yaml

INDEX_PATH = "docs/index.md"
ISSUE_BODY_PATH = "issue_body.txt"

MARKER_START = "<!-- AUTO-COOKBOOKS-START -->"
MARKER_END = "<!-- AUTO-COOKBOOKS-END -->"

def extract_fields():
    with open(ISSUE_BODY_PATH, encoding="utf-8") as f:
        lines = f.read().splitlines()

    fields = {
        "Repository URL": "",
        "Cookbook Title": "",
        "Short Description": "",
        "Thumbnail Image URL": "",
        "Root Path Name": ""
    }

    current = None
    for line in lines:
        line = line.strip().lstrip("#").strip()
        if line in fields:
            current = line
        elif current and line:
            fields[current] = line
            current = None

    return fields

def generate_card(fields):
    return f""":::{{grid-item-card}} {fields['Cookbook Title']}
:shadow: md
:link: https://katharinastarzer21.github.io/dedl-notebook-template/production/{fields['Root Path Name']}/index.html
:img-top: {fields['Thumbnail Image URL']}
{fields['Short Description']}
:::
"""

def main():
    fields = extract_fields()
    card = generate_card(fields)

    with open(INDEX_PATH, encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(
        rf"({re.escape(MARKER_START)})(.*)({re.escape(MARKER_END)})",
        re.DOTALL
    )
    match = pattern.search(content)
    if not match:
        raise RuntimeError(f"⚠️ Marker {MARKER_START} und {MARKER_END} nicht in {INDEX_PATH} gefunden!")

    new_cards = match.group(2).strip() + "\n\n" + card
    new_content = f"{MARKER_START}\n{new_cards}\n{MARKER_END}"
    final_content = content[:match.start()] + new_content + content[match.end():]

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(final_content)
    print("✅ index.md updated successfully.")

if __name__ == "__main__":
    main()
