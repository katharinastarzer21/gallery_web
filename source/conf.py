import datetime
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'EODC Knowledge Base'
copyright = f'{datetime.datetime.now().year}, EODC GmbH'
author = 'EODC GmbH'
release = '2025.9.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx_togglebutton'
]

exclude_patterns = []

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'markdown',
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


html_theme = "sphinx_nefertiti"
html_static_path = ['_static']
html_css_files = [
    'css/custom.css',
]
html_logo = "_static/eodc_logo_old.png"
html_theme_options = {
    'default_mode': 'light',
    'globaltoc_depth': 4,
    'globaltoc_collapse': True,
    'globaltoc_includehidden': True,
    'html_minify': True,
    'css_minify': True,
    'collapse_navigation': True,
}