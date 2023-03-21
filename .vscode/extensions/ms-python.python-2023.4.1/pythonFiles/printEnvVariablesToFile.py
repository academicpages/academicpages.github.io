# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
import json
import sys


# Last argument is the target file into which we'll write the env variables as json.
json_file = sys.argv[-1]

with open(json_file, "w") as outfile:
    json.dump(dict(os.environ), outfile)
