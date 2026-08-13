# Configuration file for the Sphinx documentation builder (Chinese version)
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'UVE'
copyright = '2021-2026, Saltyfish'
author = 'Saltyfish'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'content_en/overview.md']

# Language setting for Chinese
language = 'zh_CN'

# Master document
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

import os

rtd_version = os.environ.get('READTHEDOCS_VERSION_NAME')
release = rtd_version or 'development'
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "navigation_depth": 4,
    "collapse_navigation": False,
    "version_selector": True,
    "language_selector": True,
    "flyout_display": "attached",
}
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "/")
html_js_files = [
    ("readthedocs.js", {"defer": "defer"}),
]
