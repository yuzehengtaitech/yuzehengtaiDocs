# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Yuzehengtai Docs'
copyright = '2022, Yuzehengtai'
author = 'Peng'
master_doc = 'index'

# The full version, including alpha/beta/rc tags
release = 'V0.0.1'

import recommonmark
from recommonmark.transform import AutoStructify

source_suffix = ['.rst', '.md']


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'recommonmark',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_context = {
  'display_github': True,
  'github_user': 'yuzehengtai',
  'github_repo': 'yuzehengtai docs',
  'github_version': 'master/docs/',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

def setup(app):
    app.add_config_value('recommonmark_config', {
        'enable_math': True,
        'enable_inline_math': True,
        'enable_eval_rst': True,
        'enable_auto_doc_ref': False,
    }, True)
    app.add_transform(AutoStructify)
    