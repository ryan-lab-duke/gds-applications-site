# Geospatial Data Science

This repository hosts the code for the online textbook, *Geospatial Data Science* designed by [Johnny Ryan](https://www.johnny-ryan.com/).

## Repository structure

The Python package [`jupyter-book`](https://jupyterbook.org/intro.html#install-jupyter-book) processes the Jupyter notebook files from this repository and outputs them as the publication-quality HTML files that generate the [corresponding website](https://owel-lab.github.io/gds-applications-site/).

The HTML files are currently hidden in this branch of the GitHub repository, but you can find them in the [gh-pages branch](https://github.com/owel-lab/gds-applications-site/tree/gh-pages).

## Build

The book can be updated by running:

`jupyter-book build book/`

`ghp-import -n -p -f book/_build/html`

## Acknowledgments

This course was inspired by [Melanie Walsh](https://melaniewalsh.github.io/Intro-Cultural-Analytics/welcome.html), [David Shean](https://github.com/UW-GDA/gda_course_2021) and [Ryan Abernathey](https://github.com/earth-env-data-science/earth-env-data-science-book). 

## License

This book is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
