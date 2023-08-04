# Install Python Interpreter

## Pre-installed Python

By default, Windows doesn't come with Python.

Old MacOS comes with an old Python 2, you can check the version using `python --versoin`. Your MacOS may pre-install an old version Python 3, you can check the version using `python3 --version`. You should install and use the latest Python 3 edition. In MacOS, always use `python3` instead of `python`.

## Install Python3

Please download and install the latest Python 3 version from [Python Dowland Site](https://www.python.org/downloads/). The latest version is something like `3.x.y`. You can ignore the specific Python version in the following videos. It is the same process for different Python versions and Operating System versions.

### Windows

Please install the latest Python version by following the video [Install on Windows 10](https://youtu.be/UvcQlPZ8ecA). Please follow the instruction to test your installation. For example, you should be able to run `python --version` in command line to check that you install the right version.

### MacOS

Please install the latest Python version following the video [Install Python on Mac OS](https://youtu.be/TgA4ObrowRg). Make sure that you can run `python3` from the command line.

## Install Python Packages

Many useful Python software are available as packages/modules that can be installed using the `pip` or `pip3` command - they are the same.

First, you may want to upgrade your `pip` using the command `python3 -m pip install --upgrade pip`. Use `pip --version` to check that it works and displays the current version.

Then, use `pip install package-name` or `pip3 install package-name` to install a Python package, replace the `package-name` with the specific package name. For example, if you want to use `matplotlib` to plot a graph, use the command `pip install matplotlib` to install it.
