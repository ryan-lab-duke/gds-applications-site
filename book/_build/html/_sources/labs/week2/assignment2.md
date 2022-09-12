# Assignment 2

```{admonition} Deadline
Please complete this assignment before xxx.

```

Download the data for the assignment from [here](https://www.dropbox.com/sh/63dhmgtcoss1s0k/AAAsYpRdCV3xcr0jbNq9qFGZa?dl=0). The first dataset contains the centers of activity of all known Northern Spotted Owls breeding pairs in Western Oregon as determined by the Bureau of Land Management. More information can be found [here](https://databasin.org/datasets/18c5edbd64c7497aa17a369fbab6f4ac/). The second dataset contains wildfire perimeters for Oregon from the [National Interagency Fire Center](https://data-nifc.opendata.arcgis.com/search?tags=Category%2Chistoric_wildlandfire_opendata).

```{image} images/spotted_owl.jpg
:width: 400px
:align: center
```

*****************************

## Task 1 (5 points)

Import `GeoPandas`, read the **wildfire** dataset, and answer the following questions:

* a) How many rows and columns are there?

* b) How many wildfires occurred in **2021**?

Reproject the dataset to UTM Zone 10N (EPSG:32610) and make a new column called `area` that contains the **area** of each wildfire.

* c) What are the **names** and **years** of the five largest wildfires? 

* d) What was the **total area** (in km$^2$) of wildfire in **2021**?

* e) Which **five years** had the largest total area of wildfire?

*****************************

## Task 2 (5 points)

Read the **spotted owls** dataset and answer the following questions:

* a) How many rows and columns are there?

* b) What percentage of locations have **female** spotted owls?

* c) What is the furthest **north** that spotted owls have been identified?

* d) What is the furthest **east** that spotted owls have been identified?

Reproject the dataset to UTM Zone 10N (EPSG:32610).

* e) Make a new column called `pairs` which has a value of `1` if there are **both** male and female owls in that location. 

*****************************

## Task 3 (5 points)

* a) How many owl pairs were affected by wildfires between 1908 and 2021.

```{admonition} Click to reveal hint
:class: tip, dropdown
Merge the two datasets using a **spatial join**.
```

* b) In which **year** were most owl pairs affected by wildfires?

* c) How **many** owl pairs were affected in this year?

* d) Provide the **name** and **year** of the wildfire that affected the most owl pairs (disregard wildfires named `Unknown`)?

* e) Provide the **name** and **year** of the wildfire that affected the most owl pairs **per km$^2$** (disregard wildfires named `Unknown`)?

*****************************


```{important}
Save your notebook to your local course folder and submit assignment (in **.ipynb** format) to Canvas by the deadline.
```
















