# Copyright (C) 2025 Jure Cerar
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging
import winreg
import argparse
import subprocess
import re
from pathlib import Path

__author__ = "Jure Cerar"
__date__ = "25 May 2025"
__version__ = "0.1.1"


# Root directory for WSL wrappers
ROOT_DIR = Path.home().joinpath("wsl-wrappers")


def init() -> None:
    """Add WSL-Wrappers ROOT directory to user's PATH
    """
    logging.info("Adding WSL-Wrappers directory to user's PATH")
    logging.info(f"Directory: {ROOT_DIR}")
    # Get user's PATH in WIN
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment", 0, winreg.KEY_READ) as key:
        path = winreg.QueryValueEx(key, "PATH")[0]
    # Check if already in PATH
    processed_path = [Path(p).resolve() for p in path.split(";")]
    if ROOT_DIR.resolve() in processed_path:
        logging.info("The directory is already in the user's PATH")
        return
    # Add to PATH
    updated_path = ";".join([path, str(ROOT_DIR)]) if path else str(ROOT_DIR)
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment", 0, winreg.KEY_SET_VALUE) as key:
        winreg.SetValueEx(key, "PATH", 0, winreg.REG_EXPAND_SZ, updated_path)
    logging.info("The directory was added to the user's PATH")
    logging.info("You may need to log out and back in or restart your shell to see the change")


def add(alias: str, command: str = None) -> None:
    """Create a WSL wrapper for a command under given alias.
    If command is not specified alias is interpreted as command.
    Args:
        alias (str): Name of the wrapper function
        command (str): (optional) Actual command of the wrapper
    """
    if not alias:
        return ValueError("Alias must be present")
    if not command:
        command = alias
    logging.info(f"Adding wrapper alias: '{alias}' -> '{command}'")
    # Check if command is a valid WSL command
    # NOTE: Do we consider invalid command an error?
    proc = subprocess.run(["wsl", "command", "-v", *command.split()],
                          stdout=subprocess.DEVNULL)
    if proc.returncode:
        raise ValueError("Not valid WSL command")
    # Check for ROOT directory
    if not ROOT_DIR.is_dir():
        ROOT_DIR.mkdir()
    # Find template and modify it for alias
    filename = Path(__file__).parent.joinpath("template.bat")
    if not filename.is_file():
        raise FileExistsError("Cannot find template file")
    with filename.open("r") as f:
        template = f.read()
    template = template.replace("%WSL_COMMAND%", alias)
    # Write template to new alias
    filename = ROOT_DIR.joinpath(alias + ".bat")
    with filename.open("w") as f:
        f.write(template)


def rm(alias: str) -> None:
    """Remove created WSL wrapper
    Args:
        alias (str): Name of the wrapper function
    """
    if not alias:
        return ValueError("Alias must be present")
    logging.info(f"Removing alias: '{alias}'")
    # Check for directory
    if not ROOT_DIR.is_dir():
        raise ValueError("Root directory not found")
    filename = ROOT_DIR / (alias + ".bat")
    if not filename.is_file():
        raise ValueError("File not found")
    logging.debug(f"Removing file '{filename}'")
    filename.unlink()


def ls() -> None:
    """List all WSL wrappers
    """
    if not ROOT_DIR.is_dir():
        raise ValueError("WSL-wrapper not initialized")
    # List all files
    print("# WSL-Wrappers:")
    print("#")
    for file in ROOT_DIR.glob("*.bat"):
        print(file.stem)


def main():
    parser = argparse.ArgumentParser(
        description="Tool for generating and managing wrappers for calling functions from WSL in Windows.",)
    parser.add_argument("-V", "--version", action="version", version=f"%(prog)s v{__version__}",
                        help="show version information and exit")
    subparsers = parser.add_subparsers(dest="action", required=True)
    # Initialize
    subparsers.add_parser("init", help="Add WSL wrappers directory to user's PATH")
    # Add alias
    parser_add = subparsers.add_parser("add", help="Add an WSL wrapper")
    parser_add.add_argument("alias", help="Name of the alias to be added")
    parser_add.add_argument("command", type=str, nargs="?", default=None,
                            help="Actual command to be added under alias")
    # Remove alias
    parser_remove = subparsers.add_parser("remove", help="Remove an WSL wrapper")
    parser_remove.add_argument("alias", help="Name of the alias to be removed")
    # List alias
    subparsers.add_parser("list", help="List all WSL wrappers")

    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO)
    match args.action:
        case "init":
            init()
        case "add":
            add(args.alias, args.command)
        case "remove":
            rm(args.alias)
        case "list":
            ls()


if __name__ == '__main__':
    main()
