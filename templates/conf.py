# Minimal conf.py für einzelne Cookbooks in DestinE
import os
import sys
from pathlib import Path

# Optional: Erweiterungspfad für Extensions, falls du eigene nutzt
extensions = [
    "myst_nb",
    "sphinx_design",
    "sphinx.ext.githubpages",
]

project = "Cookbook"
author = "Contributors"

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# MyST / Notebooks
source_suffix = {
    ".ipynb": "myst-nb",
    ".md": "myst-nb",
    ".myst": "myst-nb",
}

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "substitution",
]
myst_heading_anchors = 3
nb_execution_mode = "off"  # wichtig für CI, keine Ausführung
nb_execution_timeout = 1800
nb_execution_allow_errors = False

# Theme: Kompatibel mit vielen Layouts
html_theme = "sphinx_book_theme"
html_title = "Cookbook Preview"
html_logo = ""
html_favicon = ""
html_static_path = ["_static"]
html_css_files = []

html_theme_options = {
    "repository_url": "",
    "use_repository_button": False,
    "use_issues_button": False,
    "use_edit_page_button": False,
    "show_navbar_depth": 2,
}

master_doc = "index"
