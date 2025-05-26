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

import setuptools
from pathlib import Path

try:
  from wsl_wrappers.wrap import __version__
except:
  print("Could not import package version")
  __version__ = None

with Path("README.md").open() as f:
    readme = f.read()

setuptools.setup(
    name="wsl-wappers",
    version=__version__ if isinstance(__version__, str) else str(__version__),
    keywords="Windows Subsystem Linux, Wrapper",
    description="Wrapper generation tool for calling Linux function with WSL",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="GNU GPL 3.0",
    python_requires=">=3.6.0",
    url="https://github.com/JureCerar/",
    author="Jure Cerar",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "wsl-wrappers=wsl_wrappers.wrap:main",
        ]
    },
    install_requires=[],
    platforms="Windows",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: Microsoft :: Windows",
    ],
    zip_safe=False,
)
