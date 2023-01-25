# Assignment 3

```{admonition} Deadline
Please complete this assignment before **Feb 3, 11:59pm** .
```

Download the data for the assignment from [here](https://www.dropbox.com/s/6nkgvgbcgu4p9b0/graph.graphml?dl=0) and [here](https://www.dropbox.com/s/6gescpjfasrny7v/oregon_cities.zip?dl=0). The first dataset is a full-featured `OSMnx`/`NetworkX` graph constructed from a shapefile of the [Oregon Highway Network](https://spatialdata.oregonexplorer.info/geoportal/details;id=1d255f740ff74774b236e0faf4d6c2e0). If you're interested, the shapefile was converted to a graph using the code [here](https://github.com/owel-lab/gds-applications-site/blob/main/book/labs/week3/convert_shp_to_multidigraph.ipynb). The second dataset is shapefile containing all cities in Oregon (as points).

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

* f) Produce **and customize** a plot showing the Oregon Highway Network using the `ox.plot_graph` function.

*****************************

## Task 2 (10 points)

Read the `oregon_cities.shp` using `GeoPandas`.

* a) Reproject the city `GeoDataFrame` to UTM Zone 10 N.

* b) Choose four cities in Oregon (the more spread out the better!) and compute the Euclidean distance (in km) between each pair.

* c) List the **nearest node** for each of the four cities.

* d) What is the shortest path length (i.e. `nx.shortest_path_length`) between **three pairs** of cities (in km)? 

* e) Produce **and customize** a plot showing the routes between your three city pairs (i.e. `fig, ax = ox.plot_graph_route(graph, route)`).

```{note}
`ox.plot_route_folium` probably will not work because the graph is not projected in the expected WGS84 coordinate system (i.e. EPSG:4326). 
```

* f) On average, how much longer is the network distances compared to the equivalent Euclidean distances? 

* g) How long would it take to travel between your three city pairs given an average speed of 60 mph?

*****************************

## Extra credit

How many cities in Oregon are within a 2 hour drive of Eugene (at 60 mph)?

*****************************

```{important}
Save your notebooks locally as both `.ipynb` and `.pdf` formats but only submit the **pdf** to Canvas.
```
















