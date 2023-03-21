import sys
from _pytest.config import get_config

c = get_config()
c.parse(sys.argv)
print(f"Python classes: {c.getini('python_classes')}")
print(f"Python files: {c.getini('python_files')}")
print(f"Python functions: {c.getini('python_functions')}")
