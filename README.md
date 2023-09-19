# Pragmatic Python Programming

## Jupyter Notebook Slides

You can show a slide in a browser by defining the following shell function `s()` and `sto()` in shell initialization script. For example, add it to `~/.zshrc` for `zsh`.

```sh
# convert and show one slide
s() {
  jupyter nbconvert $1 --to slides --post serve --SlidesExporter.reveal_scroll=True
}

# convert all to HTML slides
sto() {
  jupyter nbconvert *.ipynb --to slides --SlidesExporter.reveal_scroll=True
}
```

Then run `s file.ipynb` to do slide show in a browser. Run `sto` to convert all notebook files to HTML slides.
