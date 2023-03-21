# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import argparse
import importlib.util as import_util
import os
import pathlib
import subprocess
import sys
from typing import List, Optional, Sequence, Union

VENV_NAME = ".venv"
CWD = pathlib.PurePath(os.getcwd())


class VenvError(Exception):
    pass


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--requirements",
        action="append",
        default=[],
        help="Install additional dependencies into the virtual environment.",
    )

    parser.add_argument(
        "--toml",
        action="store",
        default=None,
        help="Install additional dependencies from sources like `pyproject.toml` into the virtual environment.",
    )
    parser.add_argument(
        "--extras",
        action="append",
        default=[],
        help="Install specific package groups from `pyproject.toml` into the virtual environment.",
    )

    parser.add_argument(
        "--git-ignore",
        action="store_true",
        default=False,
        help="Add .gitignore to the newly created virtual environment.",
    )
    parser.add_argument(
        "--name",
        default=VENV_NAME,
        type=str,
        help="Name of the virtual environment.",
        metavar="NAME",
        action="store",
    )
    return parser.parse_args(argv)


def is_installed(module: str) -> bool:
    return import_util.find_spec(module) is not None


def file_exists(path: Union[str, pathlib.PurePath]) -> bool:
    return os.path.exists(path)


def venv_exists(name: str) -> bool:
    return os.path.exists(CWD / name) and file_exists(get_venv_path(name))


def run_process(args: Sequence[str], error_message: str) -> None:
    try:
        print("Running: " + " ".join(args))
        subprocess.run(args, cwd=os.getcwd(), check=True)
    except subprocess.CalledProcessError:
        raise VenvError(error_message)


def get_venv_path(name: str) -> str:
    # See `venv` doc here for more details on binary location:
    # https://docs.python.org/3/library/venv.html#creating-virtual-environments
    if sys.platform == "win32":
        return os.fspath(CWD / name / "Scripts" / "python.exe")
    else:
        return os.fspath(CWD / name / "bin" / "python")


def install_requirements(venv_path: str, requirements: List[str]) -> None:
    if not requirements:
        return

    print(f"VENV_INSTALLING_REQUIREMENTS: {requirements}")
    args = []
    for requirement in requirements:
        args += ["-r", requirement]
    run_process(
        [venv_path, "-m", "pip", "install"] + args,
        "CREATE_VENV.PIP_FAILED_INSTALL_REQUIREMENTS",
    )
    print("CREATE_VENV.PIP_INSTALLED_REQUIREMENTS")


def install_toml(venv_path: str, extras: List[str]) -> None:
    args = "." if len(extras) == 0 else f".[{','.join(extras)}]"
    run_process(
        [venv_path, "-m", "pip", "install", "-e", args],
        "CREATE_VENV.PIP_FAILED_INSTALL_PYPROJECT",
    )
    print("CREATE_VENV.PIP_INSTALLED_PYPROJECT")


def upgrade_pip(venv_path: str) -> None:
    run_process(
        [venv_path, "-m", "pip", "install", "--upgrade", "pip"],
        "CREATE_VENV.PIP_UPGRADE_FAILED",
    )


def add_gitignore(name: str) -> None:
    git_ignore = CWD / name / ".gitignore"
    if not file_exists(git_ignore):
        print("Creating: " + os.fspath(git_ignore))
        with open(git_ignore, "w") as f:
            f.write("*")


def main(argv: Optional[Sequence[str]] = None) -> None:
    if argv is None:
        argv = []
    args = parse_args(argv)

    if not is_installed("venv"):
        raise VenvError("CREATE_VENV.VENV_NOT_FOUND")

    pip_installed = is_installed("pip")
    deps_needed = args.requirements or args.extras or args.toml
    if deps_needed and not pip_installed:
        raise VenvError("CREATE_VENV.PIP_NOT_FOUND")

    if venv_exists(args.name):
        venv_path = get_venv_path(args.name)
        print(f"EXISTING_VENV:{venv_path}")
    else:
        run_process(
            [sys.executable, "-m", "venv", args.name],
            "CREATE_VENV.VENV_FAILED_CREATION",
        )
        venv_path = get_venv_path(args.name)
        print(f"CREATED_VENV:{venv_path}")
        if args.git_ignore:
            add_gitignore(args.name)

    if pip_installed:
        upgrade_pip(venv_path)

    if args.toml:
        print(f"VENV_INSTALLING_PYPROJECT: {args.toml}")
        install_toml(venv_path, args.extras)

    if args.requirements:
        print(f"VENV_INSTALLING_REQUIREMENTS: {args.requirements}")
        install_requirements(venv_path, args.requirements)


if __name__ == "__main__":
    main(sys.argv[1:])
