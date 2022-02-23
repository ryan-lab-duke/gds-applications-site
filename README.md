# Geospatial Data Science Applications

This repository hosts the code for the online textbook, *Geospatial Data Science Applications* designed by [Johnny Ryan](https://www.johnny-ryan.com/). The textbook can be accessed at [https://owel-lab.github.io/gds-applications-site/](https://owel-lab.github.io/gds-applications-site/). 

The course introduces students to emerging geospatial data science methods for addressing important environmental challenges in the western USA. The course is taught as a series of short lectures and longer computer labs in which students will learn how to use Python to process (e.g. resampling, manipulating, interpolating), analyze (e.g. machine learning), and visualize (e.g. plotting, mapping) geospatial data. Students apply these newly developed skills to real world applications (e.g. water management, renewable energy, agriculture, hazards, and climate change). In doing so, students will become practitioners of geospatial data science who are familiar with a variety of data sources including those derived from satellite remote sensing, climate models, weather stations, census bureau, crowdsourced maps, and GPS. The course is best suited for students who already have some programming (e.g. CIS 122) and GIS (e.g. 481) experience. The skills developed during this course will be directly applicable to a career in (geospatial) data science.

Learning outcomes:

* Improve Python skills

* Learn how think computationally and statistically

* Solve real-world problems using spatial analysis

* Understand basic machine learning concepts for data science

* Manage individual and group software development using version control

* Collaborate on a group project

* Communicate results of data science project orally and as a short write-up


## Repository Structure

The Python package [`jupyter-book`](https://jupyterbook.org/intro.html#install-jupyter-book) processes the Jupyter notebook files from this repository and outputs them as the publication-quality HTML files that generate the [corresponding website](https://owel-lab.github.io/gds-applications-site/).

The HTML files are currently hidden in this branch of the GitHub repository, but you can find them in the [gh-pages branch](https://github.com/owel-lab/gds-applications-site/tree/gh-pages).

## Jupyter Book

You can learn more about Jupyter Book by exploring the documentation: https://jupyterbook.org/intro.html

## Build

The book can be updated by running:

`jupyter-book build book/`

`ghp-import -n -p -f book/_build/html`

## Acknowledgments

This course was inspired by [Melanie Walsh](https://melaniewalsh.github.io/Intro-Cultural-Analytics/welcome.html), [David Shean](https://github.com/UW-GDA/gda_course_2021) and [Ryan Abernathey](https://github.com/earth-env-data-science/earth-env-data-science-book). 

## License

This book is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
