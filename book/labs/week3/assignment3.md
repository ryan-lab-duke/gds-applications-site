# Assignment 3

```{admonition} Deadline
Please complete this assignment before xxx.
```
*****************************

## Task 1 (5 points)

Download the data for the assignment from [here](https://www.dropbox.com/s/6nkgvgbcgu4p9b0/graph.graphml?dl=0). The dataset is a full-featured `OSMnx`/`NetworkX` graph for the [Oregon Highway Network](https://spatialdata.oregonexplorer.info/geoportal/details;id=1d255f740ff74774b236e0faf4d6c2e0). If you're interested, the shapefile was converted to a graph using the code [here]().

Import the dataset using the following code:

```
import geopandas as gpd
import osmnx as ox
import networkx as nx

graph = ox.load_graphml('path/to/data/graph.graphml')
```

* a) How many nodes and edges does this graph have?

Convert the graph to two `GeoDataFrames`, one containing **edges** and one containing the **nodes**. 

```{admonition} Click to reveal hint
:class: tip, dropdown
`ox.graph_to_gdfs(graph, nodes=True, edges=False)` will provide the nodes.
```

* b) What is the coordinate reference system of the nodes `GeoDataFrame`?

* c) List the column names in the edges `GeoDataFrame`.

* d) What is the **min**, **max**, and **mean** edge length? 

* e) Produce and customize a plot showing the Oregon Highway Network graph.

```{admonition} Click to reveal hint
:class: tip, dropdown
The `ox.plot_graph` function will help.
```
*****************************

## Task 2 (5 points)



Euclidean distances between things... make sure that is covered in Lecture 2. 

Euclidean vs. network distances, what is the average difference and why? When would Euclidean distances be justified and when won't there be.






















