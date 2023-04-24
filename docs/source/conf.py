# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'GetUp Dataset'
copyright = '2023, Yochai Weissman'
author = 'Yochai Weissman'
release = '0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
                    'sphinx.ext.autosummary',
                    'sphinx.ext.napoleon',
                    'sphinx.ext.githubpages' ]
autosummary_generate = True  # Turn on sphinx.ext.autosummary


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


# -- imports ----------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join('..', '..', 'src')))
sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath(os.path.join('..', '..')))
