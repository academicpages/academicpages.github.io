# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
import builtins

try:
    import json

    try:
        from notebook.notebookapp import list_running_servers

        server_list = list_running_servers()
    except:
        from jupyter_server import serverapp

        server_list = serverapp.list_running_servers()

    server_info_list = []

    for si in server_list:
        server_info_object = {}
        server_info_object["base_url"] = si["base_url"]
        server_info_object["notebook_dir"] = si.get(
            "notebook_dir", si.get("root_dir", "")
        )
        server_info_object["hostname"] = si["hostname"]
        server_info_object["password"] = si["password"]
        server_info_object["pid"] = si["pid"]
        server_info_object["port"] = si["port"]
        server_info_object["secure"] = si["secure"]
        server_info_object["token"] = si["token"]
        server_info_object["url"] = si["url"]
        server_info_list.append(server_info_object)

    builtins.print(json.dumps(server_info_list))
except Exception:
    """Usage of subprocess is safe here as we are using run and are in control of all the arguments passed to it
    flagging for execution of partial path is also not correct as it is a command, not a path"""
    import subprocess  # nosec
    from subprocess import PIPE  # nosec
    import sys

    result = subprocess.run(  # nosec
        ["jupyter", "notebook", "list", "--jsonlist"], stdout=PIPE, stderr=PIPE
    )
    encoding = os.getenv("PYTHONIOENCODING", "utf-8")
    builtins.print.write(result.stdout.decode(encoding))
