# Assignment 3

Download the data for the assignment from [here](https://prodduke-my.sharepoint.com/:f:/g/personal/jr555_duke_edu/EoXdTF5NaLxCrYIWMAOpzDgBoKoJ2LQkcTa0mE841lyi5w?e=KuHIAJ). There are two datasets in this folder. The first, `grahph.graphml`, is a full-featured `OSMnx`/`NetworkX` graph constructed from a shapefile of the [North Carolina primary and secondary road network](https://catalog.data.gov/dataset/tiger-line-shapefile-2023-state-north-carolina-primary-and-secondary-roads). If you're interested, the shapefile was converted to a graph using the code [here](https://github.com/ryan-lab-duke/gds-applications-site/blob/main/book/labs/week3/convert_shp_to_multidigraph.ipynb). The second, `tl_2019_37_place_centroids`, is a shapefile containing centroids of all **places** in North Carolina (i.e. as points). The Census Bureau defines a place as an incorporated city, town, village, or borough. 

```{image} images/highway.jpg
:width: 500px
:align: center
```

*****************************

## Task 1 (10 points)

Read the graph dataset using the following code:

```
import geopandas as gpd
import osmnx as ox
import networkx as nx

graph = ox.load_graphml('path/to/data/graph.graphml')
```

* a) How many nodes and edges does this graph have?

* b) Convert the graph to two `GeoDataFrames`, one containing **edges** and one containing the **nodes**. 

```{admonition} Click to reveal hint
:class: tip, dropdown
`ox.graph_to_gdfs(graph, nodes=True, edges=False)` will provide the nodes.
```

* c) What is the coordinate reference system of the nodes `GeoDataFrame`?

* d) List the column names in the edges `GeoDataFrame`.

* e) What is the **min**, **max**, and **mean** edge length? 

* f) Produce **and customize** a plot showing the North Carolina road network using the `ox.plot_graph` function.

*****************************

## Task 2 (10 points)

Read the `tl_2019_37_place_centroids.shp` using `GeoPandas`.

* a) Reproject the city `GeoDataFrame` to UTM Zone 17 N.

* b) Choose four cities in North Carolina (the more spread out the better!) and compute the Euclidean distance (in km) between each pair.

* c) List the **nearest node** for each of the four cities.

* d) What is the shortest path length (i.e. `nx.shortest_path_length`) between **three pairs** of cities (in km)? 

* e) Produce **and customize** a plot showing the routes between your three city pairs (i.e. `fig, ax = ox.plot_graph_route(graph, route)`).

```{note}
`ox.plot_route_folium` probably will not work because the graph is not projected in the expected WGS84 coordinate system (i.e. EPSG:4326). 
```

* f) On average, how much longer is the network distances compared to the equivalent Euclidean distances? 

* g) How long would it take to travel between your three city pairs given an average speed of 60 mph?

*****************************

## Task 3 (5 points)

* How many cities in North Carolina are within a 2 hour drive of Durham (at 60 mph)?

*****************************

```{important}
Save your notebooks locally as both `.ipynb` and `.pdf` formats but only submit the **pdf** to Canvas.
```
















