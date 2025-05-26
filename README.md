## wsl-Wrappers

There are a lot of useful scientific programs available for Linux, but best of luck compiling it on Windows. Fortunately, Windows Subsystem for Linux (WSL) is a thing! This is a simple script that generate wrappers for calling functions from WSL in Windows.

## Installation

To install the package type the following in command line:

```shell
git clone https://github.com/JureCerar/wsl-wrappers.git
cd ./wsl-wrappers
pip install .
```

## Usage

First you need to initialize WSL-Wrappers with:

```shell
wsl-wrappers init

```

This adds WSL-Wrappers root directory (where wrappers scripts are located) to user's PATH; by default this is `%USERPROFILE%\wsl-wrappers`. Then you can add, remove, and list packages 

```shell
wsl-wrappers add ls
# INFO:root:Adding wrapper alias: 'ls' -> 'ls'
wsl-wrappers add ls 'ls -a'
# INFO:root:Adding wrapper alias: 'ls' -> 'ls -a'

wsl-wrappers list
# WSL-Wrappers:
# ls

wsl-wrappers remove ls
# INFO:root:Removing alias: ls
```

To install the package simply type:



clustalw.bat



## License

This program is licensed under the GNU General Public License v3.0

Copyright (C) 2025 [Jure Cerar](https://github.com/JureCerar)

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.