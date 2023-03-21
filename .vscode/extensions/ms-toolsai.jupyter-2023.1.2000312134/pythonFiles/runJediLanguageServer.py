import re
import sys
import os

# Add the lib path to our sys path so jedi_language_server can find its references
EXTENSION_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(EXTENSION_ROOT, "pythonFiles", "lib", "python"))

from jedi_language_server.cli import cli

# Trick language server into thinking it started from 'jedi-language-server.exe'
sys.argv[0] = "jedi-language-server.exe"
sys.exit(cli())
