# Professional Python Programming

This repository has both notes, slides, and code for learning professional Python Programming.

The notes are in markdown format. The slides are in Jupyter notebook format.

The site is built with [Material for Mkdocs](https://squidfunk.github.io/mkdocs-material/).

## Writing Tools

The following VSCode extensions are use to write the book.

- [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker): A basic spell checker that works both with markdown and code.
- [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint): it is a markdown checking tools to encourage standards the consistency for markdown files.

## Jupyter Notebook Files

The Jupyter Notebook files are used to create two types of files:

- Initial markdown content files
- book slides.

To create the initial content files and HTML slides files from notebook files, define shell function `nbm`, `nbs()` and `nbss()` in shell initialization script. For example, add them to `~/.zshrc` for `zsh`.

```sh
# create markdown files
nbm() {
  jupyter nbconvert *.ipynb --to markdown
}

# convert and show one slide
nbs() {
  jupyter nbconvert $1 --to slides --post serve --SlidesExporter.reveal_scroll=True
}

# convert all to HTML slides
nbss() {
  jupyter nbconvert *.ipynb --to slides --SlidesExporter.reveal_scroll=True
}
```
