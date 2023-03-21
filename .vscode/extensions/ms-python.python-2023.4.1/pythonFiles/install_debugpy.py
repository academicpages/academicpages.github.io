# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import io
import json
import os
import urllib.request as url_lib
import zipfile

from packaging.version import parse as version_parser

EXTENSION_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUGGER_DEST = os.path.join(EXTENSION_ROOT, "pythonFiles", "lib", "python")
DEBUGGER_PACKAGE = "debugpy"
DEBUGGER_PYTHON_ABI_VERSIONS = ("cp310",)
DEBUGGER_VERSION = "1.6.6"  # can also be "latest"


def _contains(s, parts=()):
    return any(p in s for p in parts)


def _get_package_data():
    json_uri = "https://pypi.org/pypi/{0}/json".format(DEBUGGER_PACKAGE)
    # Response format: https://warehouse.readthedocs.io/api-reference/json/#project
    # Release metadata format: https://github.com/pypa/interoperability-peps/blob/master/pep-0426-core-metadata.rst
    with url_lib.urlopen(json_uri) as response:
        return json.loads(response.read())


def _get_debugger_wheel_urls(data, version):
    return list(
        r["url"]
        for r in data["releases"][version]
        if _contains(r["url"], DEBUGGER_PYTHON_ABI_VERSIONS)
    )


def _download_and_extract(root, url, version):
    root = os.getcwd() if root is None or root == "." else root
    print(url)
    with url_lib.urlopen(url) as response:
        data = response.read()
        with zipfile.ZipFile(io.BytesIO(data), "r") as wheel:
            for zip_info in wheel.infolist():
                # Ignore dist info since we are merging multiple wheels
                if ".dist-info/" in zip_info.filename:
                    continue
                print("\t" + zip_info.filename)
                wheel.extract(zip_info.filename, root)


def main(root):
    data = _get_package_data()

    if DEBUGGER_VERSION == "latest":
        use_version = max(data["releases"].keys(), key=version_parser)
    else:
        use_version = DEBUGGER_VERSION

    for url in _get_debugger_wheel_urls(data, use_version):
        _download_and_extract(root, url, use_version)


if __name__ == "__main__":
    main(DEBUGGER_DEST)
