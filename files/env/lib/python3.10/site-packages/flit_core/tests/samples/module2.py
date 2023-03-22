"""
Docstring formatted like this.
"""

a = {}
# An assignment to a subscript (a['test']) broke introspection
# https://github.com/pypa/flit/issues/343
a['test'] = 6

__version__ = '7.0'
