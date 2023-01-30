#!/usr/bin/env python
# coding: utf-8

# # Gridded data analysis
# 
# In this demo, we will be investigating the extent of **shrubification** in Alaska using the **National Land Cover Database (NLCD)**. "Shrubification" describes the expansion of shrubs across the **Arctic**. Shrubs are woody plants with diverse growth forms but are often the tallest plants occupying tundra ecosystems and can form dense thickets with closed canopies in suitable habitats. 
# 
# Studies indicate that warming temperatures, changes in snow cover, altered disturbance regimes (due to permafrost thaw, tundra fires, anthropogenic activities or changes in herbivory intensity) are all contributing to general **increases in shrub abundance** which will have wide-ranging consequences for the ecosystems and climate of the region.
# 
# ```{image} images/shrubs.jpeg
# :width: 600px
# :align: center
# ```

# ## National Land Cover Database
# 
# The National Land Cover Database (NLCD) provides **gridded land cover** at a 30 m resolution with a **20-class legend (in Alaska)** based on a modified Anderson Level II classification system. 
# 
# The database is designed to provide cyclical updates of United States land cover every 2-3 years since 2001. 
# 
# Enables systematic documententation of land cover change for monitoring and trend assessments.
# 
# ```{image} images/nlcd-classes.jpg
# :width: 300px
# :align: center
# ```

# ## Gridded data
# 
# Gridded (or raster) data represent a matrix of cells (or pixels) organized into rows and columns (or a grid). Grid cells can represent data that changes **continuously** across a landscape (surface) such as elevation, air temperature, or . reflectance data from satellite imaging platforms. Grid cells can also represent **discrete** data such as vegetation type or land cover.
# 
# ```{image} images/raster-matrix.png
# :width: 500px
# :align: center
# ```

# ## Libraries
# 
# The main library for accessing and analyzing gridded data in Python is called `rasterio` which builds on the popular **Geographic Raster Abstraction Library** or **GDAL**. It supports read/write access for over 160 gridded data formats (e.g. GeoTIFF, NetCDF4) and includes methods for finding dataset information, reprojecting, resampling, format conversion, and mosaicking. 
# 
# ```{image} images/gdal.png
# :width: 200px
# :align: center
# ```
# 
# Let's get started...

# In[2]:


# Import libraries
import numpy as np
import rasterio
import pandas as pd
import matplotlib.pyplot as plt


# ## Open dataset
# 
# The data is formatted as a GeoTIFF (`.tif`) file which is one of the many formats that can be read by `rasterio`. We can open the dataset using the function `open()` which accepts a **path string** and returns a **dataset object**.

# ```{note}
# The data for this demo can be accessed [here](https://www.dropbox.com/sh/czfmie4piindv8n/AAAiZCdIoi9dSqVTIHK0c8yPa?dl=0).
# ```

# ````{margin}
# ```{note}
# `src` stands for **source**
# ```
# ````

# In[28]:


src = rasterio.open('data/nlcd_2016_ak.tif')
src


# ## Dataset attributes
# 
# The **dataset object** contains a number of **attributes** which can be explored using the following methods. Remember that a raster **band** is an array of values representing **a single** variable in 2D space. All bands of a dataset have the **same** number of rows and columns.

# In[29]:


print(f"Number of bands: {src.count}")
print(f"Width: {src.width}")
print(f"Height: {src.height}")
print(f"Data type: {src.dtypes}")


# ## Georeferencing
# 
# Like vector data, pixels in raster data can be mapped to regions on the Earth's surface. Like `GeoPandas`, we can display the **coordinate reference system** of our data using the `crs` method. 

# In[21]:


src.crs


# The output from this function can be a little overwelming but there is some useful information contained here. For example it looks like the data are projected using an [**Albers projection system**](https://en.wikipedia.org/wiki/Albers_projection) and the units are in **meters**. 
# 
# We can display some more specific information about a dataset's projection using the `transform` method. This function returns the **spatial resolution** of the dataset (i.e. the dimensions that each pixel of our dataset represents on the ground) and the coordinates of the **top left** corner.

# In[22]:


src.transform


# Alternatively, we can display the bounding box of our dataset using the `bounds()` method.

# In[23]:


src.bounds


# ## Reading raster data
# 
# Now that we have some basic information, we can go ahead and import our data as a NumPy **N-D array** using the `read()` function. Data from each band can be accessed by an index number. 

# ```{note}
# Note that bands are indexed from 1 due to a  GDAL convention. 
# ```

# In[24]:


nlcd_2016 = src.read(1)
nlcd_2016


# In[25]:


type(nlcd_2016)


# ## Plot data
# 
# We can have a look at the data using `matplotlib`. Since the dataset is so big (eight billion pixels!), we will just plot a subset of the data.

# In[30]:


fig, ax = plt.subplots(figsize=(16,8))
im = ax.imshow(nlcd_2016, cmap='tab20b')
ax.set_title("Alaska land cover", fontsize=14)


# ## Single land cover type
# 
# It would be useful to identify what some of these colors mean. To do this we can use **matrix indexing** to find the value of a pixel at a given location (i.e. `array[row, column]`). In this case we find the land cover at **y (or row) = 500** and **x (or column) = 3000**. 

# In[37]:


nlcd_2016[500, 3000]


# The land cover type is **52** meaning **shrub/scrub**. 
# 
# ```{image} images/nlcd-shrubs.png
# :width: 800px
# :align: center
# ```

# In[34]:


fig, ax = plt.subplots(figsize=(16,8))
im = ax.imshow(nlcd_2016, cmap='tab20b')
ax.scatter(3000, 500, s=100, color='k')
ax.set_title("Alaska land cover", fontsize=14)


# ## Frequency of land cover type
# 
# Clearly shrubs (class 52) cover a large portion the land cover in this region of Alaska. To **quantify** how much area they cover, it would be useful to count the **occurrence of each land cover class**. We can do that using NumPy's [`unique()`](https://numpy.org/doc/stable/reference/generated/numpy.unique.html) function, making sure we set `return_counts` to `True`. 

# In[40]:


unique, counts = np.unique(nlcd_2016, return_counts=True)
dict(zip(unique, counts))


# In[42]:


# Count number of land pixels
land_pixels = nlcd_2016.size

# Convert to DataFrame
df_2016 = pd.DataFrame(list(zip(unique, counts, (counts/land_pixels)*100)), 
                       columns=['lc', 'count_2016', 'fraction_2016'])
df_2016


# This is very useful. With reference to the NLCD land cover classes, our table shows that the most dominant type of land cover is **dwarf shrub** (51) at **22%** althoug **normal shrubs** (52) are not far behind with **17%**. We also have some **evergreen forest** (42) at **13%** and **woody wetlands** (90) at **10%**. 
# 
# ```{image} images/nlcd-classes.jpg
# :width: 300px
# :align: center
# ```

# ## Aggregate land cover classes
# 
# Since we are interested in shrubs of all kinds shrubs, we will combine the the **dwarf shrubs** and **shrub/scrub** classes. The most simple way of doing this is to re-assign all grid cells classified as **shrub/scrub** (52) to **dwarf shrubs** (51) using a **mask**.

# In[43]:


# Re-assign land cover class
nlcd_2016[nlcd_2016 == 52] = 51


# In[44]:


# Check there are no more grid cells classified as normal shrubs
unique, counts = np.unique(nlcd_2016, return_counts=True)

# Convert to DataFrame
df_2016 = pd.DataFrame(list(zip(unique, counts, (counts/land_pixels)*100)), 
                       columns=['lc', 'count_2016', 'fraction_2016'])
df_2016


# ## Land cover change
# 
# The big question here is have these shrubs always occupied a large portion of this region of Alaska? To answer that we could perform the same analysis on a previous NLCD dataset from 2001.

# In[46]:


# Open
src_2001 = rasterio.open('data/nlcd_2001_ak.tif')

# Read
nlcd_2001 = src_2001.read(1)

# Re-assign land cover class
nlcd_2001[nlcd_2001 == 52] = 51


# In[47]:


# Count occurrence in each class
unique, counts = np.unique(nlcd_2001, return_counts=True)

# Convert to DataFrame
df_2001 = pd.DataFrame(list(zip(unique, counts, (counts/land_pixels)*100)),
                       columns=['lc', 'count_2001', 'fraction_2001'])
df_2001


# Combining the DataFrames should allow us to compute the difference between 2001 and 2016

# In[48]:


df = pd.merge(df_2001, df_2016, on=['lc'])
df


# In[49]:


df['change'] = (df['count_2016'] - df['count_2001'])
df['change_percent'] = (((df['count_2016'] - df['count_2001']) / df['count_2001']) * 100)
df


# ## Conclusion
# 
# Oh dear - the extent of shrubs did **not** increase between 2001 and 2016. One takeway from this could be that shrubification is **not happening** in this region of the Arctic. But the percentage change in shrubs was very small (-0.02%) and could well be smaller than the uncertainty in our land cover product. For example, if just 1% of pixels were incorrectly classified as shrubs in 2001 our result would be insignificant. 
# 
# Other, peraps more signficant changes, that occurred between 2001 and 2016 include an increase in **deciduous forest** (41) by **3.9%**, a decrease in **evergreen forest** (42) by **0.4%**, and an decrease in **emergent herbaceous wetlands** (95) by **0.4%**. 

# ## Direction of land cover change
# 
# It would be interesting to know **how** grid cells changed between 2001 and 2016. We can do this by **masking** the 2016 land cover data with specific grid cells from the 2001 land cover data. For example, in the code below we identify grid cells in 2016 that were classified as **evergreen forest** (class 42) in 2001. We then compute what land cover they are by **masking the 2016 land cover data** and using the `unique()` function.

# In[50]:


mask = nlcd_2016[nlcd_2001 == 42]
unique, counts = np.unique(mask, return_counts=True)


# In[51]:


forestchange_df = pd.DataFrame(list(zip(unique, counts, (counts/mask.shape[0])*100)),
                 columns=['lc', 'count', 'fraction'])
forestchange_df


# It looks like most of the **evergreen forest** (99.6%) did not change between 2001 and 2016. When it did, it was most likely to change to **shrub** (51) which may indicate some "shrubification" in Alaska. Let's finish this section by plotting a map showing where **evergreen forest** was replaced by **shrub**.

# In[52]:


forest2shrub = (nlcd_2001 == 42) & ((nlcd_2016 == 51))


# In[73]:


fig, ax = plt.subplots(figsize=(16,8))
im = ax.imshow(forest2shrub.astype(int), cmap='Blues')
ax.set_title("Fores to shrubs in Alaska between 2001 and 2016", fontsize=14)


# At this scale, it's difficult to see what's going on. Let's zoom in a little...

# In[72]:


fig, ax = plt.subplots(figsize=(16,8))
im2 = ax.imshow(forest2shrub.astype(int)[1000:1750,2750:3750], cmap='Blues')
ax.set_title("Forest to shrubs in Alaska between 2001 and 2016", fontsize=14)


# In[ ]:




