# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


import os
import sys
import pathlib

path = pathlib.Path(__file__).resolve() / '..' / ".."
sys.path.insert(0, os.path.abspath(path))


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Project Name'
copyright = 'ZK-TE-A Advanced Analytics'
author = 'ZK-TE-A Advanced Analytics'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinxcontrib.images',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
images_config = {
    'override_image_directive': True,
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = '_static/logo.png'


def skip(app, what, name, obj, would_skip, options):
    if name == "__init__":
        return False
    return would_skip


def setup(app):
    # Include custom css file (e.g. for background color)
    app.add_css_file('custom.css')

    # Use custom skip method so that the __init__ method is always shwon
    # in the documentation
    app.connect("autodoc-skip-member", skip)
