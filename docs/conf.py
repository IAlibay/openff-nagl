# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

# In case the project was not installed
import openff.nagl
import os
import sys

sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = 'OpenFF NAGL'
copyright = "2021+ Open Force Field Initiative"
author = "Open Force Field Initiative"

# The short X.Y version
version = openff.nagl.__version__
# The full version, including alpha/beta/rc tags
release = openff.nagl.__version__


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "openff_sphinx_theme",
    "myst_nb",
]

# Autodoc settings
autosummary_generate = True

autodoc_default_options = {
    "members": True,
    "inherited-members": True,
    "member-order": "bysource",
}
autodoc_preserve_defaults = True
autodoc_typehints_format = "short"
# Workaround for autodoc_typehints_format not working for attributes
# see https://github.com/sphinx-doc/sphinx/issues/10290#issuecomment-1079740009
python_use_unqualified_type_names = True

napoleon_numpy_docstring = True
napoleon_google_docstring = False
napoleon_attr_annotations = True
napoleon_custom_sections = [("attributes", "params_style")]
napoleon_use_rtype = False
napoleon_use_param = True

_python_doc_base = "https://docs.python.org/3.7"
intersphinx_mapping = {
    "python": ("https://docs.python.org/3.7", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference", None),
    "scikit.learn": ("https://scikit-learn.org/stable", None),
    "openmm": ("http://docs.openmm.org/latest/api-python/", None),
    "rdkit": ("https://www.rdkit.org/docs", None),
    "openeye": ("https://docs.eyesopen.com/toolkits/python/", None),
    "mdtraj": ("https://www.mdtraj.org/1.9.5/", None),
    "openff.interchange": (
        "https://docs.openforcefield.org/projects/interchange/en/stable/",
        None,
    ),
    "openff.fragmenter": (
        "https://docs.openforcefield.org/projects/fragmenter/en/stable/",
        None,
    ),
}
myst_url_schemes = [
    "http",
    "https",
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Extensions for the myst parser
myst_enable_extensions = [
    "dollarmath",
    "colon_fence",
    "smartquotes",
    "replacements",
    "deflist",
]
myst_heading_anchors = 3

# Myst NB settings
# Execute all notebooks on build
nb_execution_mode = "force"
# List of notebooks NOT to execute (use output stored in notebook instead)
nb_execution_excludepatterns = []

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = [".rst", ".md", ".ipynb"]

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'default'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "openff_sphinx_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.

html_theme_options = {
    # Repository integration
    # Set the repo url for the link to appear
    "repo_url": "https://github.com/openforcefield/openff-nagl",
    # The name of the repo. If must be set if repo_url is set
    "repo_name": "openff-nagl",
    # Must be one of github, gitlab or bitbucket
    "repo_type": "github",
    # Colour for sidebar captions and other accents. One of
    # openff-toolkit-blue, openff-dataset-yellow, openff-evaluator-orange,
    # red, pink, purple, deep-purple, indigo, blue, light-blue, cyan,
    # teal, green, light-green, lime, yellow, amber, orange, deep-orange
    "color_accent": "openff-toolkit-blue",
    # Content Minification for deployment, prettification for debugging
    "html_minify": False,
    "html_prettify": False,
    "css_minify": True,
    "master_doc": False,
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default:
html_sidebars = {
    "**": ["globaltoc.html", "searchbox.html", "localtoc.html"],
}



# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'openff-nagldoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'openff-nagl.tex', 'OpenFF NAGL Documentation',
     'openff-nagl', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'openff-nagl', 'OpenFF NAGL Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'openff-nagl', 'OpenFF NAGL Documentation',
     author, 'openff-nagl', 'A short description of the project.',
     'Miscellaneous'),
]


