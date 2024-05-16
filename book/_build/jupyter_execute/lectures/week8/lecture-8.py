#!/usr/bin/env python
# coding: utf-8

# # Automating raster analysis
# 
# In this class we have, for the most part, been working with relatively tidy datasets. For example, vector datasets with no missing values, gridded datasets that have consistent dimensions. But in the real-world, datasets are often messy. When conducting a research project, therefore, most of our time is actually spent formatting data so that it is convenient to analyze. This includes making sure that gridded data has the same dimensions, grid cell sizes, and projections. In this activity, we will coach you through a typical workflow that we would use for analyzing many satellite images.
# 
# ## Background
# 
# We have been asked to compute the seasonal variability in surface water for a small region just North of Anchorage, Alaska. To do this, we have downloaded satellite imagery from [Planet Lab's](https://www.planet.com/) constellation of CubeSats. The images can be downloaded from [here](XXX). These images contain four bands (Red, Green, Blue, and Near-Infrared) with a pixel resolution of ~3 m. Unfortunately, the images are not tiled meaning that the images have different numbers of rows and columns. This will prevent us applying statistical analysis to images as a whole. Furthermore, the images are projected in a geographic coordinate system (i.e. degrees) meaning that any area calculation will be inaccurate. The goal of this activity is to reformat the images to a common standard and track how surface water varies through time. Proceed by following the set of instructions below.

# ## Task 1
# 
# * a) Download the data to your course folder
# 
# * b) Import `rasterio` and `os` packages
# 
# * c) Make a **sorted** list of files in the directory where you saved the data
# 
# ```{admonition} Click here for hint
# :class: tip, dropdown
# The [`os.listdir](https://docs.python.org/3/library/os.html#os.listdir)` function returns a list containing the names of the entries in the directory. The [`sorted()`](https://www.w3schools.com/python/ref_func_sorted.asp) function returns a sorted list. 
# ```
# 
# * d) What is the list

# In[ ]:


import glob
import rasterio
import os


# In[25]:


path = '/Users/johnnyryan/Dropbox (University of Oregon)/teaching/gds-applications-site/resources/data/petersville/'
files = sorted(os.listdir(path))
len(files)


# In[32]:


for file in files:
    filepath = path + file
    src = rasterio.open(filepath)
    print(f"Width: {src.width} and Height: {src.height}")


# In[35]:


for file in files:
    filepath = path + file
    src = rasterio.open(filepath)
    print(src.bounds)


# In[36]:


src.transform


# ## Convert datatype to minimum size
# 

# In[13]:


(4*4)+(4*8)


# In[14]:


(3*4)+(3*4)


# In[ ]:




