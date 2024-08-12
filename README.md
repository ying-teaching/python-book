# Professional Python Programming

This repository has both notes, slides, and code for learning professional Python Programming.

The notes are in markdown format. The slides are in Jupyter notebook format.

The site is built with [Material for Mkdocs](https://squidfunk.github.io/mkdocs-material/).

## Writing Tools

The following VSCode extensions are use to write the book.

- [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker): a basic spell checker that works both with markdown and code.
- [Markdown Lint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint): it is a markdown checking tools to encourage standards the consistency for markdown files.
- [Jupyter Slide Show](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.vscode-jupyter-slideshow): adding slide types to notebook.

## Jupyter Notebook Files

The Jupyter Notebook files are used to create two types of files:

- Initial markdown content files
- book slides.

To add slide type to a cell, open the command palette (Cmd+Shift+P) and select `Switch Slide Type`. It is better to add a key shortcut `Ctrl + Shift + S` for the operation.

To create the initial content files and HTML slides files from notebook files, define shell function `nbm()`, `nbs()` and `nbss()` in shell initialization script. For example, add them to `~/.zshrc` for `zsh`. Run these commands in the the `.ipynb` file folder.

```sh
# create markdown files
nbm() {
  jupyter nbconvert *.ipynb --to markdown
}

# convert and show one slide
nbs() {
  jupyter nbconvert $1 --to slides --post serve --SlidesExporter.reveal_scroll=True
}

# convert all ipynb files to HTML slides
nbss() {
  jupyter nbconvert *.ipynb --to slides --SlidesExporter.reveal_scroll=True
}
```
