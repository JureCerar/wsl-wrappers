## WSL-Wrappers

There are a lot of useful (scientific) software available for Linux, but best of luck compiling it on Windows systems. Fortunately, Windows Subsystem for Linux (WSL) is a thing now! You don't need to install software on Windows you just need it to install it in WSL and then create a wrapper that can call it from Windows. This is a simple tool to generate and manage wrappers. 

## Installation

To install the package type the following in command line:

```shell
git clone https://github.com/JureCerar/wsl-wrappers.git
cd ./wsl-wrappers
pip install .
```

## Example

First you need to initialize WSL-Wrappers with:

```shell
wsl-wrappers init
```

This adds WSL-Wrappers root directory (by default this is `%USERPROFILE%\wsl-wrappers`) to user's PATH. Then you can add, remove, and list wrappers with: 

```shell
wsl-wrappers add jackhmmer
# Adding wrapper alias: 'jackhmmer' -> 'jackhmmer'

wsl-wrappers list
# WSL-Wrappers:
# jackhmmer

wsl-wrappers remove jackhmmer
# INFO:root:Removing alias: 'jackhmmer'
```

> [!NOTE]
> Needless to say you need to have WSL installed on your system to use this tool. Follow these instructions on [How to install WSL](https://learn.microsoft.com/en-us/windows/wsl/install). You also need to install software within WSL in order to call it (obviously), e.g. `jackhmmer`.

## License

This program is licensed under the GNU General Public License v3.0

Copyright (C) 2025 [Jure Cerar](https://github.com/JureCerar)

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.