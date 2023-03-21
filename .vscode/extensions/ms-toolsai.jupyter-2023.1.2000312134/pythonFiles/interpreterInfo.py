# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import json
import sys
import builtins

obj = {}
obj["versionInfo"] = tuple(sys.version_info)
obj["sysPrefix"] = sys.prefix
obj["version"] = sys.version
obj["exe"] = sys.executable
obj["is64Bit"] = sys.maxsize > 2**32

builtins.print(json.dumps(obj))
