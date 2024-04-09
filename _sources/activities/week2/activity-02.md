# Activity 2

```{admonition} Deadline
Please complete this assignment before **Apr 17 11:59pm**.

```

Download the data for the assignment from [here](https://www.dropbox.com/scl/fo/otgc923zyn2o8go10486e/h?rlkey=jmzcte1fddpic85a78eju6tfx&dl=0). This dataset contains population and income data for Census tracts in Lane County, Oregon. In this activity, we will use the `geopandas` package to do some basic analysis on this dataset. 

```{note}
`B01003_001` is **population** and `B19301_001` is **household income**. 
```

```{image} images/lane-county.png
:width: 200px
:align: center
```
*****************************

* Activate the `.gds` Python environment by opening an **Anaconda Prompt (miniconda3)** (Windows) or **Terminal** (macOS). Then, on Windows:

```
.gds\Scripts\activate
```

Or, on macOS:

```
source .gds/bin/activate
```

```{note}
Make sure you run this command from the **same directory** as the `.gds` environment folder.
```

* Open a Jupyter Notebook by running:

```
jupyter notebook
```

```{tip}
If you run this command from your course folder, your `.ipynb` assignment will automatically be saved there.
```


*****************************

## Task 1 (5 points)

Import the `geopandas` package and read the shapefile. Write some code that prints the following information:

* Number of columns

* Number of rows

* The maximum `B01003_001` value

* The minimum `B19301_001` value

* The mean `B19301_001` value

*****************************

## Task 2 (5 points)

* Reproject the shapefile to a `projected coordinate system` (i.e. spatial units are in meters)

* Make a new column that contains population density (in km2).

* What is the min, mean, and max population density?

*****************************

## Task 3 (5 points)

* Make a chloropleth map showing population density

```{admonition} Click to reveal hint
:class: tip, dropdown
The following guide may be helpful: https://geopandas.org/en/stable/docs/user_guide/mapping.html
```

* Make a chloropleth map showing household income.

* Customize both plots so they look more presentable.

*****************************

```{important}
Save your notebook locally in both `.ipynb` and `.pdf` formats but only submit the **pdf** to Canvas.
```











