# Install Python Interpreter

If you are not an advanced user, please follow the instructions here to install the latest Python 3 software. Advanced users can install `Anaconda` -- it is not recommended for new developers because it requires more knowledge to use it.

## Python 3 vs Python 2

You need a Python interpreter to run your Python program. The first task of learning Python is installing Python in your computer. There are two major versions of Python: Python 2 and Python 3 and they are not fully compatible. Python 2 can not run Python 3 program and vice versa. There are many Python 2 programs but Python 2 is no longer developed, you shoud learn Python 3.

By default, Windows doesn't come with Python.

MacOS comes with an old Python 2, you can check the version using `python --versoin`. The MacOS may pre-install an old version Python 3, you can check the version using `python3 --version`. You should install and use the lastes Python 3 edition. In MacOS, alwasy use `python3` instead of `python`. Simailary, if you want to try built-in IDLE programming enviornment, run `idle3` in your terminal.

## The Latest Python 3 Installation

Please download and install the latest Python 3 version from [Python Dowland Site](https://www.python.org/downloads/). The latest version is something like `3.x.y`. You can ignore the specific Python version in the following videos. The steps should be similar for all Python 3 versions.

### Windows

Please install the latest Python version following the video [How to Install Python 3.10.4 on Windows 10](https://youtu.be/UvcQlPZ8ecA). Run `python --version` to check that you install the right version.

### MacOS

Please install the latest Python version following the video [How to install Python on Mac OS](https://youtu.be/TgA4ObrowRg). Make sure that you can run `python3` from the command line. For advanced user, you can check the [Using Python on a Macintosh](https://docs.python.org/3/using/mac.html).

## Install Python Packages

Many useful Python software are avaialabe as packages/modules that can be installed using the `pip` or `pip3` commmand - they are the same.

First, you may want to upgrade your `pip` using the command `python3 -m pip install --upgrade pip`. Use `pip --version` to check that it works and displays the current version.

Then, use `pip install package-name` or `pip3 install package-name` to install a Python package, replace the `package-name` with the specific package name. For example, if you want to use `matplotlib` to plot a graph, use the command `pip install matplotlib` to install it.
