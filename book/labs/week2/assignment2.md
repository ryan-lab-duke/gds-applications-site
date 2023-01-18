# Assignment 2

```{admonition} Deadline
Please complete this assignment before **Jan 27 11:59pm**.

```

Download the data for the assignment from [here](https://www.dropbox.com/sh/63dhmgtcoss1s0k/AAAsYpRdCV3xcr0jbNq9qFGZa?dl=0). The first dataset contains wildfire perimeters for Oregon from the [National Interagency Fire Center](https://data-nifc.opendata.arcgis.com/search?tags=Category%2Chistoric_wildlandfire_opendata). The first second contains the centers of activity of all known Northern Spotted Owls breeding pairs in Western Oregon as determined by the Bureau of Land Management. More information can be found [here](https://databasin.org/datasets/18c5edbd64c7497aa17a369fbab6f4ac/). 

```{image} images/spotted_owl.jpg
:width: 400px
:align: center
```
*****************************

## Task 0 (0 points)

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

```{note}
If you run this command from your course folder, your `.ipynb` assignment will automatically be saved there.
```

*****************************

## Task 1 (5 points)

Import `GeoPandas`, read the **wildfire** dataset, and answer the following questions:

* a) How many rows and columns are there?

* b) How many wildfires occurred in **2021**?

```{admonition} Click to reveal hint
:class: tip, dropdown
Remember the syntax for masking is `df[df['column'] == value]`.
```

* c) Reproject the dataset to UTM Zone 10N (EPSG:32610) and make a new column called `area` that contains the **area** of each wildfire.

* d) What are the **names** and **years** of the five largest wildfires? 

* e) What was the **total area** (in km$^2$) of wildfire in **2021**?

```{note}
The units of the `area` column are m$^2$ by default.
```

*****************************

## Task 2 (5 points)

Read the **spotted owls** dataset and answer the following questions:

* a) How many rows and columns are there?

* b) What is the min/max values in the `males` and `females` columns?

* c) What percentage of locations have **female** spotted owls?

* d) What is the furthest **east** that spotted owls have been identified?

Reproject the dataset to UTM Zone 10N (EPSG:32610).

* e) Make a new column called `pairs` which has a value of `1` if there are **both** male and female owls in that location. 

*****************************

## Task 3 (5 points)

* a) How many owl pairs were affected by wildfires?

```{admonition} Click to reveal hint
:class: tip, dropdown
Merge the two datasets using a **spatial join**. Depending on how you do it, there will be rows with `NaN` values. These are wildfires that don't overlap with owls (or owls that don't overlap with wildfires). Before computing stats, we recommend removing these using the [`.dropna()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html#pandas-dataframe-dropna) method.
```

* b) In which **year** were most owl pairs affected by wildfires?

```{admonition} Click to reveal hint
:class: tip, dropdown
The `.groupby` method will be very useful here. 
```

* c) How **many** owl pairs were affected in this year?

* d) Provide the **name** and **year** of the wildfire that affected the most owl pairs (disregard wildfires named `Unknown`)?

* e) Make a plot showing locations of Northern Spotted Owls breeding pairs on top of the wildfire perimeters for Oregon.

*****************************

## Extra credit

There are several duplicate records in the wildfire dataset and the names of fires are inconsistent - some are all caps for example. For extra credit, clean up this dataset by:

* Converting wildfire names to lower case

* Ignoring wildfires named **UNKNOWN** or **UNNAMED** (or similar), remove duplicated rows (i.e. same name and year) keeping the larger of the two wildfire areas

* Save as a shapefile and send to me via email.


```{important}
Save your notebooks locally as both `.ipynb` and `.pdf` formats but only submit the **pdf** to Canvas.
```
















