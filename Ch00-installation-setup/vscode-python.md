# Install and Setup VS Code for Python Development

## Python Development Tools

Python also comes with two built-in development tools: the Python interpreter and the IDLE programming environment (`idle` in Windows, `idle3` in Mac OS). Both allow you interact with Python to write and run code. They are very simple and has limited functions. Therefore you only use them for simple tasks.

Professional developers use IDE (integrated development environment) to edit, run and debug programs. [JetBrains' PyCharm](https://www.jetbrains.com/pycharm/) is a popular and good IDE but the professional PyCharm edition is not free.

VS Code might be the best and free development tool for Python programming and it is getting better every month. VS code supports multiple programming languages and can handle many development tasks such as file editing, running and debugging. It has a huge amount of extensions that can do most development tasks you need to do.

## Install VS Code

Go to [VS Code docs](https://code.visualstudio.com/docs) to learn and install VS Code for your operating system. It should be easy but in case you are not sure, you can check the following resources.

- For Windows, follow the [VS Code on Windows](https://code.visualstudio.com/docs/setup/windows) or watch the video [How to Install VS Code 2020](https://youtu.be/7yLXtkSsRKE).
- For Mac OS, follow the [VS Code on macOS instruction](https://code.visualstudio.com/docs/setup/mac) or watch the video [How to Install VS Code on Mac](https://youtu.be/IATbkNl8qng).

Programmers often run VS Code from the command line. There is an extra step to enable this in Mac OS. Please follow the instruction in [launching form the command line](https://code.visualstudio.com/docs/setup/mac#_launching-from-the-command-line).

## Learn VS Code

VS code has a rich set of editing features and it is extensible. Click `Help -> Welcome`, you can see the Welcome screen. It has shortcuts to create a new file, open a folder, recent projects and a lot help information.

You should find time to go through the first 5 videos in [Introductory Videos](https://code.visualstudio.com/docs/getstarted/introvideos) to learn the basic functions such as user interface, extensions, shortcut keys, code editing, file operations, and settings. Though examples are JavaScript or text files, most operations are the same for other program languages. The more you know about the VS code, the more efficient you will be. You should invest time to learn it. In addition to the five vidoes, You should also read the following sections

- [Tips and Tricks](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)
- [User Interface](https://code.visualstudio.com/docs/getstarted/userinterface)
- [User and Workspace Settings](https://code.visualstudio.com/docs/getstarted/settings)

For detail information about a specific feature, check the [VS Code User Guide](https://code.visualstudio.com/docs/editor/codebasics). You should be familiar with the functions described in the first four sections: Basic Editing, Extension Marketplace, IntelliSense, and Code Navigation.

## Setup Python for VS Code

VS Code has powerful support for Python programming. You need to install the [Microsoft Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python). Be caerful to install the Microsoft extention -- it is the best.

To see an installation/setup demo, you can watch one of the following videos:

- For Widnows, [VS Code Python Setup Windows 10](https://youtu.be/Jd4trL90HSw)
- For Mac OS, [Setup Python For Visual Studio Code - macOS](https://youtu.be/veJvQ88ULOM). Please make sure that VS code uses the Python 3 you installed, not the Python 2 coming with Mac OS.

## Develop Python Program in VS Code

You should start with the [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial) and try our the examples in the tutorial. For new developers, you don't need to create virtual environment as described in the last section in the document. You can skip step 1 and 2 and directly install `matplotlib` in command line. In both Windows and Mac OS, just run `pip install matplotlib` and you should be able to run a plot application.

## Jupyte Notebook

The Jupyter Notebook is useful to write note that mixes Markdown text and Python code. It is very popular among data scientists. [Data Science in VS Code](https://code.visualstudio.com/docs/datascience/overview) is the document to use Jupyte Notebooks in VS Code. The VS code Jupyte-related extensions are installed when you install the Python extension.

## Learning Resources

The following two videos from Microsoft VS code tema are a good introduction to programming Python in VS Code.

- [Getting Started with Python in Visual Studio Code](https://channel9.msdn.com/Shows/Visual-Studio-Toolbox/Getting-Started-with-Python-in-Visual-Studio-Code)
- [Jupyter Notebooks in Visual Studio Code](https://channel9.msdn.com/Shows/Visual-Studio-Toolbox/Jupyter-Notebooks-in-Visual-Studio-Code)

It seems that VS Code keeps improving every day and there are new features/changes that are inconsistent with the above documents and videos. But the essentail ideas are there.

## Markdown Document

This document and many software projects use Markdown format to write documents. Markdown is a text format standard that is widely used by programmers. You can [Master Markdown](https://guides.github.com/features/mastering-markdown/) in about 10 minutes.
