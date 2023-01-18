#!/usr/bin/env python
# coding: utf-8

# # Vector data analysis
# 
# The vector data model represents space as a series of discrete entities such as such as borders, buildings, streets, and roads. There are three different types of vector data: points, lines and polygons. Online mapping applications, such as **Google Maps** and **OpenStreetMap**, use this format to display data. 
# 
# The Python library `GeoPandas` provides somes great tools for working with vector data. As the name suggests, `GeoPandas` extends the popular data science library `Pandas` by adding support for geospatial data. The core data structure in `GeoPandas` is the `GeoDataFrame`. The key difference between the two is that a `GeoDataFrame` can store geometry data and perform spatial operations.
# 
# ```{image} images/dataframe.png
# :alt: geodataframe
# :width: 700px
# :align: center
# ```
# 
# The `geometry` column can contain any geometry type (e.g. points, lines, polygons) or even a mixture.

# ## Reading files
# 
# Assuming we have a file containing both data and geometry (e.g. GeoPackage, GeoJSON, Shapefile), we can read it using `read_file`, which automatically detects the filetype and creates a `GeoDataFrame`. In the this demo, we will be working with three shapefiles containing 1) cities and towns (as points), 2) urban growth boundaries (as polygons), and 3) counties (as polygons) in Oregon. 

# In[2]:


import os
os.environ['USE_PYGEOS'] = '0'
import geopandas as gpd

cities = gpd.read_file('data/oregon_cities.shp')
cities.head()


# ## DataFrame properties
# 
# We can analyze our `GeoDataFrame` using standard `Pandas` functions.

# In[3]:


# Data types of each column
cities.dtypes


# In[4]:


# Number of rows and columns
cities.shape


# In[5]:


# Name of columns
cities.columns


# ## Indexing
# 
# We can select specific columns based on the column values. The basic syntax is `dataframe[value]`, where `value` can be a single column name, or a list of column names.

# In[6]:


# List the city names
cities['name']


# In[7]:


# List the latitudes and longitudes
cities[['lat','lon']]


# We can select specific rows using the `.iloc` method.

# In[8]:


# Second row
cities.iloc[1]


# In[9]:


# Sixth to tenth rows
cities.iloc[5:10]


# ## Masking
# 
# We can sample of our `DataFrame` based on specific values by producing a **Boolean mask** (i.e. a list of values equal to `True` or `False`). To find cities that are East of -117.5 degrees longitude, we could write:

# In[10]:


mask = cities['lon'] > -117.5
cities[mask]


# It's more concise to just add the Boolean mask between square brackets. Here we find a specific city.

# In[11]:


cities[cities['name'] == 'Eugene']


# Or cities that contain a `z` in their name. 

# In[12]:


cities[cities['name'].str.contains('z')]


# ## Descriptive statistics
# 
# `Pandas` provides basic functions to calculate descriptive statistics.

# In[96]:


# Minimum latitude value
cities['lat'].min()


# In[97]:


# Mean longitude value
cities['lon'].mean()


# A full list of descriptive statistics (including some very useful ones such as `sum` and `count`) can be found [here](https://pandas.pydata.org/docs/user_guide/basics.html#descriptive-statistics).
# 
# Sometimes we want to know which row contains the specific value which we can do using `idxmax`/`idxmin`.

# In[98]:


cities['lat'].idxmin()


# In[99]:


cities.iloc[232]


# ## Sorting
# 
# We can sort `DataFrames` using the `sort_values` function. This function takes two arguments, `by` and `ascending` which determine which column and which order we would like to sort by. 

# In[100]:


# Find the ten most northerly cities in Oregon
cities.sort_values(by='lat', ascending=False).head(10)


# An alternative way of doing this would be to use the `nlargest/nsmallest` functions.

# In[101]:


cities.nlargest(n=10, columns='lat')


# ## Geometric properties
# 
# The special thing about a `GeoDataFrame` is that it contains a `geometry` column. We can therefore apply spatial methods to these data. To demonstrate we will use our Oregon county shapefile. 

# In[224]:


# Read shapefile
counties = gpd.read_file('data/orcntypoly.shp')


# In[225]:


counties['area'] = counties['geometry'].area
counties.head()


# We produced an `area` column but we were warned because our data are in a **geographic coordinate refrence system (CRS)**... 

# ## Projections
# 
# `GeoDataFrames` have their own **CRS** which can be accessed using the [`crs`](https://geopandas.org/en/stable/docs/user_guide/projections.html) method. The CRS tells `GeoPandas` where the coordinates of the geometries are located on the Earth's surface. 

# In[226]:


counties.crs


# We can reproject a our data using the `to_crs` method.

# In[227]:


counties_reproject = counties.to_crs('EPSG:32610')
counties_reproject.crs


# Now our data has a **projected CRS**, we can calculate the area of each county with no warnings.

# In[228]:


counties_reproject['area'] = counties_reproject['geometry'].area
counties_reproject.head()


# In[229]:


counties_reproject.nlargest(n=10, columns='area')


# ## More geometric properties
# 
# There are other spatial methods we can apply to polygons such as the length of the outer edge (i.e. perimeter). 

# In[230]:


counties_reproject['perimeter'] = counties_reproject['geometry'].length
counties_reproject.head()


# Our `cities` `GeoDataFrame` also has geometric properties. We can access the latitude and longitude using the `x` and `y` methods.

# In[231]:


cities['geometry'].x


# In[232]:


cities['geometry'].y


# ## Measure distance
# 
# We can measure the distance between two points, provided they have a projected CRS.

# In[233]:


cities_reproject = cities.to_crs('EPSG:32610')


# In[234]:


eugene = cities_reproject[cities_reproject['name'] == 'Eugene'].reset_index()
bend = cities_reproject[cities_reproject['name'] == 'Bend'].reset_index()


# In[235]:


eugene.distance(bend).values[0] / 1000


# We can even compute the distance from Eugene to all cities in Oregon. We just have to convert our Eugene `GeoDataFrame` to a `shapely` `Point` object.

# In[236]:


from shapely.geometry import Point
point = Point(eugene['geometry'].x, eugene['geometry'].y)
type(point)


# In[237]:


cities_reproject.distance(point)


# In[238]:


cities_reproject['dist_from_eugene'] = cities_reproject.distance(point) / 1000 


# In[239]:


cities_reproject.nsmallest(n=10, columns='dist_from_eugene')


# ## Plot
# 
# If our data are in the same projection system, we can plot them together.

# In[240]:


ax = counties_reproject.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')
cities_reproject.plot(ax=ax, color='black', markersize=5)


# ## Spatial joins
# 
# One of the most useful things about `GeoPandas` is that it contains functions to perform **spatial joins** to combine two `GeoDataFrames` based on the **spatial relationships** between their geometries.
# 
# The order of the two `GeoDataFrames` is quite important here, as well as the `how` argument. A **left** outer join implies that we are interested in **retaining the geometries** of the `GeoDataFrame` on the left, i.e. the **point** locations of the cities. We then retain attributes of the **right** `GeoDataFrame` if they intersect and drop them if they don't.
# 
# The following would provide the county attributes for all our cities based on a spatial intersection. 

# In[241]:


cities_reproject.sjoin(counties_reproject, how="left").head()


# ```{note}
# The `geometry` column type is `POINT`.
# ```

# On the other hand, a **right** outer join implies that we are interested in **retaining the geometries** of the `GeoDataFrame` on the right, i.e. the **polygons** of the counties. This time we keep all rows from the right `GeoDataFrame` and duplicate them if necessary to represent multiple hits between the two dataframes.

# In[242]:


cities_reproject.sjoin(counties_reproject, how="right").head()


# ## Which county contains the most cities/towns?
# 
# We would do this would be to use the `groupby` function.

# In[243]:


join = cities_reproject.sjoin(counties_reproject, how="left")


# The first argument `groupby` accepts is the column we want group our data into (`county` in our case). Next, it takes a column (or list of columns) to summarize. Finally, this function does nothing until we specify **how** we want to group our data (`count`).
# 
# It's actually nice to **reset the index** after using `groupby` so that we end up with a DataFrame (rather than a Series). 

# In[244]:


grouped = join.groupby('county')['name'].count().reset_index()
grouped.nlargest(n=10, columns='name')


# ## Which county is furthest from Eugene?

# In[245]:


grouped = join.groupby('county')['dist_from_eugene'].mean().reset_index()
grouped.nlargest(n=10, columns='dist_from_eugene')

