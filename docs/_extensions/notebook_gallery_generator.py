#from gallery_generator import build_from_repos, generate_menu, generate_repo_dicts
from yaml import load
import pathlib
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

def clean_f_string(string):
    return '\n'.join([m.lstrip() for m in string.split('\n')])

def build_from_repos(repos):
    grid_cards = []
    for repo_id, repo in repos.items():
        new_card = f"""
            :::{{grid-item-card}} {repo['title']}
            :shadow: md
            :link: {repo['url']}
            :img-top: {repo['thumbnail']}
            {repo['description']}
            :::
        """
        grid_cards.append(clean_f_string(new_card))
   
    grid_cards = "\n".join(grid_cards)

    grid_body = f"""
        ::::{{grid}} 2
        :gutter: 3
        {grid_cards}
        ::::
    """
    return clean_f_string(grid_body)
    

def main(app):
    import pathlib

    srcdir = pathlib.Path(app.srcdir)
    confdir = pathlib.Path(app.confdir)

    main_md_path = srcdir / "main.md"
    if not main_md_path.exists():
        print("Skipping notebook gallery generatorno main.md found.")
        return
    
    main_md_path = srcdir / "main.md"
    main_content = main_md_path.read_text() + "\n\n"

    gallery_path = confdir.parent / "notebook_gallery.yaml"
    with gallery_path.open() as fid:
        config = load(fid, Loader=Loader)

    grid = build_from_repos(config["domains"])
    main_content += grid

    index_path = srcdir / "index.md"
    if index_path.is_file():
        index_path.unlink()
    index_path.write_text(main_content)

def setup(app):
    app.connect("builder-inited", main)