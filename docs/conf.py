# Default Sphinx config for imported cookbooks
import os
import sys
import pathlib

sys.path.insert(0, os.path.abspath("_extensions"))

extensions = [
    "sphinx.ext.githubpages",
    "myst_nb",
    "sphinx_design",
]

project = 'DestinE Cookbook'
author = 'Contributors'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', "**/.git", ".pixi**", "book/**"]

source_suffix = {
    ".ipynb": "myst-nb",
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

myst_url_schemes = ["http", "https", "mailto"]
myst_heading_anchors = 3
nb_execution_mode = 'off'
nb_execution_timeout = 3600
nb_execution_allow_errors = False

html_theme = 'pydata_sphinx_theme'
html_title = "DestinE Cookbook"
html_logo = ""
html_favicon = ""
html_static_path = ['_static']
html_css_files = ['custom.css']

html_theme_options = {
    "navigation_with_keys": True,
    "show_nav_level": 2,
    "navigation_depth": 2,
    "collapse_navigation": True,
}
master_doc = 'index'