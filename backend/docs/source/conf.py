import os
import sys
from pathlib import Path

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.insert(0, project_root)

# Adiciona a pasta 'backend' ao sys.path também, caso suas importações internas a utilizem como base
backend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.insert(0, backend_path)

# Verifique se o caminho está correto
print(f"Project root added to sys.path: {project_root}")
print(f"Backend path added to sys.path: {backend_path}")
print(f"Current Python path: {sys.path}")

# -- Project information -----------------------------------------------------
project = 'Weather Watcher'
copyright = '2025, Brian Villanova and Caique Silva'
author = 'Brian Villanova and Caique Silva'
version = '1.0'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
language = 'pt'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'

# -- Extension configuration -------------------------------------------------
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
todo_include_todos = True