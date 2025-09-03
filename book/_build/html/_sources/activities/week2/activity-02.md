# Activity 2

Flooding is the most common and damaging natural disaster in the United States. Therefore understanding the number of people at risk of flooding is critical information for planning. In this activity, we will perfom some basic spatial analysis using the `geopandas` package to investigate the number of people exposed to flooding in Orange County, NC. 

The data can be downloaded from [here](https://prodduke-my.sharepoint.com/:f:/g/personal/jr555_duke_edu/EiD2lKkUb1dMsiE33eggj4MBk_tFp8z54O_aoCcobahsjQ?e=zsuzEI). There are two shapefiles in this directory. The first dataset, `orange-county-structures.shp`, is an inventory of all structures larger than 450 square feet produced by the Federal Emergency Management Agency (FEMA). More information about this dataset can be found [here](https://gis-fema.hub.arcgis.com/pages/usa-structures). The second dataset, `S_FLD_HAZ_AR.shp`, is the FEMA Special Flood Hazard Area (SFHA) designation, a regulatory product produced using 1-dimensional flood modeling. 

```{image} images/flooding.png
:width: 600px
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

Import the `geopandas` package and read the `orange-county-structures.shp` shapefile. Write some code that prints the following information from the GeoDataFrame:

* Number of rows and columns

* Coordinate reference system as an EPSG code

```{admonition} Click to reveal hint
:class: tip, dropdown
One way of getting the EPSG code from a Coordinate Reference System (CRS) object is to use the `to_epsg()` method.
```

* The number of different categories in the `OCC_CLS` column

* The percentage of buildings classified as **Residential** in the `OCC_CLS` column

```{note}
More information about the column names can be found [here](https://www.fema.gov/sites/default/files/2020-02/FIRM_Database_Technical_Reference_Feb_2019.pdf)
```

* The total number of people living in Orange County (i.e. using the `POP_MEDIAN` columns)

*****************************

## Task 2 (5 points)

Now read the `S_FLD_HAZ_AR.shp` shapefile. Write some code that prints the following information from the GeoDataFrame:

* Number of rows and columns

* Coordinate reference system as an EPSG code

Reproject the GeoDataFrame to a `projected coordinate system` (i.e. spatial units are in meters)

```{admonition} Click to reveal hint
:class: tip, dropdown
Consider using a UTM Zone e.g. [https://epsg.io/32617](https://epsg.io/32617).
```

* What is the total area of the Orange County according to this dataset (in km2)? 

* What percentage of the county (by area) has been designated as a Special Flood Hazard Area (i.e. where columns `SFHA_TF == T`)? 

*****************************

## Task 3 (5 points)

Make sure that both datasets have a common `projected coordinate system` and answer the following questions.

* How many structures **intersect** designated Special Flood Hazard Areas (i.e. where columns `SFHA_TF == T`)?

```{admonition} Click to reveal hint
:class: tip, dropdown
The [`sjoin`](https://geopandas.org/en/stable/docs/reference/api/geopandas.sjoin.html) function should work well for this.
```
* How many of these structures are classified as **Residential**?

* How many people in Orange County live in a Special Flood Hazard Area?

* Find the name of the school that is located in a Special Flood Hazard Area (2 points)

```{admonition} Click to reveal hint
:class: tip, dropdown
The `PRIM_OCC` column describes the primary occupancy for each structure. Consider finding a lat/lon first and then use Google Maps.
```

*****************************

```{important}
Save your notebook locally in both `.ipynb` and `.pdf` formats but only submit the **pdf** to Canvas.
```

## Acknowledgements

This activity was inspired by Gold and Steinberg-McElroy (2025).

Gold, A.C., Steinberg-McElroy, I. High-resolution estimates of the US population in fluvial or coastal flood hazard areas. Sci Data 12, 1377 (2025). [https://doi.org/10.1038/s41597-025-05717-y](https://www.nature.com/articles/s41597-025-05717-y)









