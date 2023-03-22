# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

# six is not a direct dependency of this module
# This replicates six.text_type
try:
    text_type = unicode
except NameError:
    text_type = str


try:
    string_types = basestring
except NameError:
    string_types = str
