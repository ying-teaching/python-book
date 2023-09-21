# Professional Python Programming

This repository has both notes, slides, and code for learning professional Python Programming.

The notes are in markdown format. The slides are in Jupyter notebook format.

The site is built with [Material for Mkdocs](https://squidfunk.github.io/mkdocs-material/).

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
