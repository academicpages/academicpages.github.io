# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.


class UnsupportedToolError(ValueError):
    def __init__(self, tool):
        msg = "unsupported tool {!r}".format(tool)
        super(UnsupportedToolError, self).__init__(msg)
        self.tool = tool


class UnsupportedCommandError(ValueError):
    def __init__(self, cmd):
        msg = "unsupported cmd {!r}".format(cmd)
        super(UnsupportedCommandError, self).__init__(msg)
        self.cmd = cmd
