# Python

In order to execute Python code for completing assignments, we will need to install a Python distribution with the necessary packages. We will use `conda`, an open-source package management system which can be installed using Miniconda (a lightweight version of [Anaconda](https://www.anaconda.com/products/individual)). 

## Install Miniconda

The latest version of Miniconda can be accessed from the [dowload page](https://docs.conda.io/en/latest/miniconda.html). In this course we will be using **Python 3.8** so download the corresponding package for your operating system.

## Test installation

After installation is complete, we can test that the package manager `conda` works by opening an **Anaconda Powershell Prompt (miniconda3)** (Windows) or **Terminal** (Mac). 

In the command prompt (or Terminal) run the following:
```
conda --version
```

If the command returns a version number of conda (e.g. `conda 4.11.0`) everything is working correctly.

## Create course environment

The Python libraries needed for this course can be installed using an `environment.yml` file which can be downloaded from [here](https://www.dropbox.com/s/x6md9xh7brma0lf/environment.yml?dl=0). 

We can install `environment.yml` by opening a Windows command prompt (as admin) or Mac terminal and running the following command:

```
conda env create -f environment.yml
```

````{margin}
```{note}
More information about managing environments can be found [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).
```
````

This will take some time but, if all goes well, we will have a new environment called `gds`. To activate this environment, type:

```
conda activate gds
```

To deactivate this environment, type:

```
conda deactivate
```

```{note}
It is possible to complete this course without installing anything on your own computer. Look for the ![](https://mybinder.org/badge_logo.svg) button on the notebooks to run the code interactively in a browser.
```



