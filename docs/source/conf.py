# Copyright 2024 NXP
# SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
# Licensed under the Solderpad Hardware License v 2.1 (the "License"); you may not use this file except in compliance with the License, or, at your option, the Apache License version 2.0.
# You may obtain a copy of the License at https://solderpad.org/licenses/SHL-2.1/

# Unless required by applicable law or agreed to in writing, any work distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Specification Process Data -----------------------------------------------

states = (
          'Development',
          'Review',
          'Release Candidate',
          'Release',
          )
state_postfix = [
                '-dev',
                '-dev',
                '-rc',
                '',
                ]

title_prefix = 'OpenHW Group Specification'

# -- Project information -----------------------------------------------------

project = u'Core-V eXtension interface (CV-X-IF)'
copyright = u'2021-2024 OpenHW Group'
author = u'OpenHW Group'
# State must be one of Development, Release Candidate, or Release
state = 'Development' 

# The short vX.Y.Z version
version = u'v0.9.0'
# If release candidate, provide release candidate version (integer)
rc_version = 1

# -- Derived Project Information - Do not modify ------------------------------

if state == 'Release Candidate' or state == 'Release':
    if version[0] == '0':
        raise ValueError(f'Version {version} not allowed for state {state}.')

postfix = state_postfix[states.index(state)]
if state == 'Release Candidate':
    postfix += f'.{rc_version}'

# The full version, including alpha/beta/rc tags
release = f'{version}{postfix}'
version = release

title = f'{title_prefix}: {project} - {state}'
filename = f'{title_prefix}_{project}_{release}'.replace(' ', '_')


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'recommonmark',
    'sphinxcontrib.inkscapeconverter',
    'sphinx_github_changelog',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['ytemplates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# Numbering
numfig=True
numfig_format = {'figure': 'Figure %s', 'table': 'Table %s', 'code-block': 'Listing %s'}

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None

# Entries for text replacement
rst_epilog = f"""
.. |title| replace:: {title}
.. |copyright| replace:: {copyright}
.. |processor| replace:: CPU
.. |processors| replace:: CPUs
.. |coprocessor| replace:: coprocessor
"""

# Tags for conditional text

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {'style_nav_header_background': '#DDDDDD', 'prev_next_buttons_location': 'both'}
html_show_sphinx = False
html_show_sourcelink = False
html_logo = '../images/openhw-landscape.svg'
html_favicon ='../images/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['ystatic']
# Set html_static_path to null on the advice of RTDs:
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

html_css_files = [
  'css/custom.css',
]

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = f'{filename}'


# -- Options for LaTeX output ------------------------------------------------

latex_logo = '../images/openhw-landscape.png'

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
    'atendofbody': f'Copyright © {copyright}'
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, f'{filename}.tex', title,
     author, 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, f'{filename}.tex', title,
     author, 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, f'{filename}.tex', title,
     author, 'Specification', title,
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = title

# The unique identifier of the text. This can be a ISBN number
# or the title homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
