# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

try:
    from notebook import notebookapp as app

    print("Available")
except Exception:
    print("No")
