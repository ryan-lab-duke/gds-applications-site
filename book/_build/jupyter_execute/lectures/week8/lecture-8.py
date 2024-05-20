#!/usr/bin/env python
# coding: utf-8

# # Automating raster analysis
# 
# In this class we have, for the most part, been working with relatively tidy datasets. For example, vector datasets with no missing values, gridded datasets that have consistent dimensions. But in the real-world, datasets are often messy. When conducting a research project, therefore, most of our time is actually spent formatting data so that it is convenient to analyze. This includes making sure that gridded data has the same dimensions, spatial resolution, and projections. In this activity, we will coach you through a typical workflow that we would use for analyzing many satellite images.
# 
# ## Background
# 
# The goal of the activity is to compute the seasonal variability in surface water for a small region just North of Anchorage, Alaska. To do this, we have downloaded satellite imagery from [Planet Lab's](https://www.planet.com/) constellation of CubeSats. The images can be downloaded from [here](https://www.dropbox.com/scl/fo/t2bqd9811kn7y4brrsfoj/AGvCU_pJY3BujkZAQwE8GM0?rlkey=glpeflxxmwq8ggwh1c4gea8lh&st=w02v80y8&dl=0). These images contain four bands (Red, Green, Blue, and Near-Infrared) with a pixel resolution of ~3 m. Unfortunately, the images are not tiled meaning that the images have different numbers of rows and columns. This will prevent us doing calculations on the whole set of images. Furthermore, the images are projected in a geographic coordinate system (i.e. degrees) meaning that any area calculation will be inaccurate. In this activity, we will learn how to use [`rioxarray`](https://corteva.github.io/rioxarray/stable/getting_started/getting_started.html) to format the images to a common standard and track how surface water varies through time. `rioxarray` is a relatively new library that extends the spatial capabilities of `xarray` using functions from `rasterio`. It's a little clunky, as we'll see, but also incredibly powerful for geospatial analysis. Proceed by following the set of instructions below.

# ## Task 1 (5 points)
# 
# * a) Download the data to your course folder
# 
# * b) Make a **sorted** list of files in the directory where you saved the data
# 
# ```{admonition} Click here for hint
# :class: tip, dropdown
# Something like [`os.listdir'](https://docs.python.org/3/library/os.html#os.listdir)` or [`glob`](https://docs.python.org/3/library/glob.html) would be useful for this. The [`sorted()`](https://www.w3schools.com/python/ref_func_sorted.asp) function returns a sorted list. 
# ```
# 
# * c) How many files are in the list?

# ## Task 2 (5 points)
# 
# First we want check the projections of the files. If they are in a geographic coordinate system then we will want to reproject them to a projected coordinate reference system. 
# 
# * a) Import the `rioxarray` package as `rio`.
# 
# * b) Open the first file in your list (i.e. `2023-07-01_strip_6617511_composite.tif`)
# 
# ```{admonition} Click here for hint
# :class: tip, dropdown
# The data can be opened using [`rio.open_rasterio(filepath)`](https://corteva.github.io/rioxarray/html/getting_started/getting_started.html#rioxarray). 
# ```
# * c) What is the coordinate system of this satellite image?
# 
# ```{admonition} Click here for hint
# :class: tip, dropdown
# The coordinate reference system can be accessed using [`.rio.crs`](https://corteva.github.io/rioxarray/html/getting_started/crs_management.html#Accessing-the-CRS-object).
# ```
# 
# * d) Reproject this satellite image to UTM Zone 5N.
# 
# ```{admonition} Click here for hint
# :class: tip, dropdown
# The EPSG code for UTM Zone 5N is **32605**. The dataset can be reprojected using [`.rio.reproject()`](https://corteva.github.io/rioxarray/html/examples/reproject.html#Reproject) and written to a new file using [`.rio.to_raster()`](https://corteva.github.io/rioxarray/stable/examples/convert_to_raster.html#Converting-Dataset-to-raster).
# ```

# ## Task 3 (5 points)
# 
# Now we want check the extents of the reprojected files to make sure they match each other.
# 
# * a) Match the extent (and projection) of the second satellite image in your list (i.e. `2023-07-13_strip_6645417_composite.tif`) with the first satellite image in your list (`2023-07-01_strip_6617511_composite.tif`).
# 
# ```{tip}
# The [`.rio.reproject_match()`](https://corteva.github.io/rioxarray/stable/examples/reproject_match.html#Example---Reproject-Match-(For-Raster-Calculations/Stacking)) is very useful for this task.  
# ```
# 
# * b) Print the number of rows and columns of both satellite images (to confirm they are all the same).

# ## Task 4 (5 points)
# 
# Next we will classify water in the images.
# 
# * a) Classify the first satellite image into three categories (i.e. null vs. water vs. non-water) using a threshold of 500 in the NIR band (i.e. band 4). Null values should be == 0, water pixels should have a value of <500 (but larger than 0) and non-water pixels should be >500.
# 
# ```{admonition} Click here for hint
# :class: tip, dropdown
# It's sometimes easier to do this by first converting Band 4 into a `NumPy` array (i.e. `dataset1_utm_np = dataset1_utm[3,:,:].values`)
# ```
# 
# * b) Calculate the fraction of water cover (i.e. as a percentage of water + non-water pixels).
# 
# * c) Write a for loop that computes water fraction for every satellite image in the list and saves it as a list.
# 
# * d) Plot the water fraction.

# ```{note}
# Congratulations for getting this far. There are still a couple of things we could do to improve this analysis. For example, accounting for cloud cover or a more sophisticated water classification. But that would take a lot of time and, for a class activity, we've done pretty well already.
# ```

# ```{important}
# Save your notebook locally in both `.ipynb` and `.pdf` formats but only submit the **pdf** to Canvas.
# ```

# In[ ]:




