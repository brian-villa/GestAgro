import os
import sys

# Adicionar caminhos para encontrar os módulos
sys.path.insert(0, os.path.abspath('../..'))  # backend/
sys.path.insert(0, os.path.abspath('../../..'))  # GestAgro/

# Configurações do projeto
project = 'GestAgro'
copyright = '2024, Seu Nome'
author = 'Seu Nome'
release = '1.0.0'

# Extensões necessárias
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
]

# Mock para dependências externas que podem não estar instaladas
autodoc_mock_imports = [
    'requests',
    'flask',
    'websockets',
    'asyncio',
    'pandas',
    'numpy',
    'datetime',
    'json',
    'typing',
    'pydantic',
    'fastapi',
    'uvicorn',
    'pytest',
    'sqlalchemy',
    'aiofiles',
]

# Configurações de template e build
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Tema HTML
html_theme = 'alabaster'
html_static_path = ['_static']

# Configurações do autodoc
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

# Configurações do Napoleon para docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False

# Configurações HTML adicionais
html_title = f"{project} Documentation"
html_short_title = project