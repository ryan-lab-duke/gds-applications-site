#!/usr/bin/env python
# coding: utf-8

# # Gridded data
# 
# * Quick review of raster data 
# <br>
# <br>
# * Introduce `rasterio` and `xarray` libararies
# <br>
# <br>
# * Learn how to read, inspect, manipulate, and write climate data
# <br>
# <br>
# * Background for this week's lab

# ## Libraries
# 
# * There is one library for accessing raster data:
# 
# The **Geographic Raster Abstraction Library** or **GDAL**
# 
# * GDAL is written in C++ and ships with a C API.
# 
# * ArcGIS, QGIS, Google Earth etc. all use GDAL to read/write/analyze raster data under-the-hood
# 
# ```{image} images/gdal.png
# :alt: raster matrix
# :width: 200px
# :align: center
# ```
# 

# ## GDAL
# 
# * Supports read/write access for over **160 raster formats** (e.g. GeoTIFF, NetCDF4)
# 
# 
# * Includes methods for:
# 
#     * Finding dataset information
#     
#     * Reprojecting
#     
#     * Resampling
#     
#     * Format conversion
#     
#     * Mosaicking
#     
# ## Rasterio
# 
# * Developed in 2016 with the goal of expressing GDAL's data model in a more Pythonic way
# 
# 
# * High performance, lower cognitive load, **more transparent code**
# 

# ## NumPy
# 
# * Major Python library for performing operations on **matrices**
# 
# 
# ```{image} images/numpy.png
# :alt: numpy
# :width: 300px
# :align: center
# ```
# 
# ## xarray
# 
# * Introduces labels in the form of **dimensions**, **coordinates** and **attributes** on top of raw NumPy-like arrays
# 
# ```{image} images/xarray.png
# :alt: xarray
# :width: 300px
# :align: center
# ```
# 
# 

# ## Let's get started...

# In[7]:


# Import libraries
import numpy as np
import xarray as xr

import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


# `xarray` is the recommended package for reading, writing, and analyzing scientific datasets stored in `.nc` or `hdf` format.
# 
# Scientific datasets include climate and satellite data.
# 
# 
# ```{image} images/xarray_data_structures.png
# :alt: xarray_data
# :width: 600px
# :align: center
# ```

# In[8]:


# Read data
xds = xr.open_dataset('data/era_jul_dec_2020.nc')


# In[9]:


# Plot
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(14,4))

im1 = ax1.imshow(xds['t2m'][0,:,:], cmap='RdYlBu_r')
im2 = ax2.imshow(xds['t2m'][1,:,:], cmap='RdYlBu_r')

ax1.set_title("Air temp. Jul 2020", fontsize=14)
ax2.set_title("Air temp. Dec 2020", fontsize=14)

divider = make_axes_locatable(ax2)
cax = divider.append_axes('right', size='5%', pad=0.05)
fig.colorbar(im2, cax=cax, orientation='vertical')


# ### Indexing multi-dimensional datasets
# 
# Since our `xarray` dataset is aware of the latitude and longitude coordinates, we can index values conveniently.

# In[10]:


# Temperature at Kathmandu
temp = xds['t2m'].sel(latitude=27.7, longitude=85.3, method='nearest')


# In[11]:


print('Jul 2020 air temperature = %.2f F' %((temp[0] - 273.15) * 9/5 + 32))
print('Dec 2020 air temperature = %.2f F' %((temp[1] - 273.15) * 9/5 + 32))


# ### Where is the coldest place on Earth (in Dec 2020)?

# In[12]:


# .argmin() returns the indices of the minimum values of an array
min_value = xds['t2m'][1,:,:].argmin()
print(min_value)


# In[13]:


# Convert 1D index to 2D coordinates
low_idx = np.unravel_index(min_value, xds['t2m'][1,:,:].shape)
print(low_idx)


# In[14]:


cold = xds['t2m'][1, low_idx[0], low_idx[1]].values
print('Coldest place on Earth was %.2f F' % ((cold - 273.15) * 9/5 + 32))


# In[15]:


# Plot
fig, ax1 = plt.subplots(figsize=(14,4))

im1 = ax1.imshow(xds['t2m'][1,:,:], cmap='RdYlBu_r')

ax1.set_title("Air temp. Dec 2020", fontsize=14)
ax1.scatter(low_idx[1], low_idx[0], s=100, color='k')

divider = make_axes_locatable(ax2)
cax = divider.append_axes('right', size='5%', pad=0.05)
fig.colorbar(im1, cax=cax, orientation='vertical')

