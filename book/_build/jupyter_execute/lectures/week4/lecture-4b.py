#!/usr/bin/env python
# coding: utf-8

# # Climate data analysis
# 
# In this demo, we will be investigating the **world's climate**. The data contains **gridded monthly air temperature and precipitation** for the 1959-2021 time period from the [Copernicus Climate Change Service](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels-monthly-means?tab=overview). 
# 
# ```{image} images/climate.jpeg
# :width: 600px
# :align: center
# ```

# ## `xarray`
# 
# * The best Python package for this task is `xarray` which introduces labels in the form of **dimensions, coordinates, and attributes** on top of raw NumPy-like arrays, a bit like `Pandas`. 
# 
# 
# * `xarray` can be used read, write, and analyze any scientific datasets stored in `.nc` or `.hdf` format.
# 
# 
# * Almost all climate data (and some remote sensing data) are stored in these formats.
# 
# ```{image} images/xarray.png
# :alt: xarray
# :width: 500px
# :align: center
# ```

# In[1]:


# Import package
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Read data
xds = xr.open_dataset('data/world_climate.nc')


# ```{note}
# The data for this demo can be accessed [here](https://www.dropbox.com/sh/czfmie4piindv8n/AAAiZCdIoi9dSqVTIHK0c8yPa?dl=0).
# ```

# ## Basic information about `Dataset`

# In[113]:


type(xds)


# In[114]:


xds.dims


# In[115]:


xds.coords


# All information can be printed using the `keys()` function. 

# In[116]:


xds.keys


# ```{note}
# `t2m` stands for 2 m above the surface, the standard height used by temperature sensors. It is a common metric used in climatology but note that it is different from the surface temperature which would be the temperature of the ground surface.
# ```

# Since we are using an interactive notebook, a more convenient way of finding information about our dataset is to just execute the variable name.

# In[117]:


xds


# ## Basic information about `DataArray`
# 

# In[12]:


type(xds['latitude'])


# In[13]:


xds['latitude']


# Print as a NumPy array

# In[14]:


type(xds['latitude'].values)


# First item in array

# In[15]:


xds['latitude'].values[0]


# Last item in array

# In[16]:


xds['latitude'].values[-1]


# Shape of `DataArray`

# In[17]:


xds['latitude'].values.shape


# ## Time

# In[18]:


type(xds['time'].values[0])


# In[19]:


period = xds['time'].values[-1] - xds['time'].values[0]
period


# In[20]:


period.astype('timedelta64[Y]')


# Convert to **integer**

# In[21]:


period.astype('timedelta64[Y]').astype(int)


# ## Plot

# In[24]:


fig, ax = plt.subplots(figsize=(10,6))

im1 = ax.imshow(xds['t2m'][0,:,:], cmap='RdYlBu_r')

ax.set_title("Air temperature", fontsize=14)
divider = make_axes_locatable(ax)
cax = divider.append_axes('right', size='5%', pad=0.05)
fig.colorbar(im1, cax=cax, orientation='vertical')


# ## Stats
# 
# Compute mean air temperature for entire period

# In[25]:


temp = xds['t2m']
mean_temp = temp.mean(['time'])
mean_temp


# In[26]:


mean_temp.shape


# In[28]:


mean_temp[300, 100]


# In[29]:


# Plot
fig, ax = plt.subplots(figsize=(10,6))

im1 = ax.imshow(xds['t2m'][0,:,:], cmap='RdYlBu_r')
ax.scatter(100, 300, s=100, c='k')

ax.set_title("Air temperature", fontsize=14)
divider = make_axes_locatable(ax)
cax = divider.append_axes('right', size='5%', pad=0.05)
fig.colorbar(im1, cax=cax, orientation='vertical')


# ## Indexing multi-dimensional datasets
# 
# Since our `xarray` dataset is **aware** of the latitude and longitude coordinates, we can index values conveniently.

# In[30]:


t = xds['t2m'].sel(latitude=27.7, longitude=85.3, method='nearest')
print('The mean annual air temperature in Kathmandu is %.2f F' %((t.mean('time').values - 273.15) * 9/5 + 32))


# Convert to Pandas `DataFrame`

# In[31]:


t.to_dataframe()


# ## Where is the coldest place on Earth (1959-2021)?
# 
# To find the coldest place on Earth we have to find the grid cell with the lowest temperature. The `argmin()` function returns the **indices** of the minimum values of an array. 

# In[38]:


min_value = mean_temp.argmin()
print(min_value)


# Perhaps unexpectedly, `argmin()` returns a single number instead of a row/column pair. We can use NumPy's `unravel_index()` to convert this 1D index to 2D coordinates. It just needs to know the **shape** of our original 2D `DataArray`.

# In[39]:


low_idx = np.unravel_index(min_value, mean_temp.shape)
print(low_idx)


# In[40]:


cold = mean_temp[low_idx[0], low_idx[1]].values
print('Coldest place on Earth is %.2f F' % ((cold - 273.15) * 9/5 + 32))


# In[41]:


fig, ax1 = plt.subplots(figsize=(10,6))

im1 = ax1.imshow(xds['t2m'][1,:,:], cmap='RdYlBu_r')

ax1.set_title("Coldest place on Earth (1959-2021)", fontsize=14)
ax1.scatter(low_idx[1], low_idx[0], s=100, color='k')

divider = make_axes_locatable(ax1)
cax = divider.append_axes('right', size='5%', pad=0.05)
fig.colorbar(im1, cax=cax, orientation='vertical')


# ## Which was the hottest month on Earth (1959-2021)?
# 
# To find the hottest month on Earth, we need to preserve the time dimension of our data. Instead we need average over the latitude and longitude dimensions.  

# In[42]:


hot = xds['t2m'].mean(['longitude','latitude'])


# In[43]:


hot['time'][hot.argmax()].values


# Which was July 2019!!

# ## Which was the hottest year on Earth (1959-2021)?
# 
# There are a couple of ways to find the hottest year. The first is to use the `groupby` function. 

# In[44]:


temp_yearly = xds['t2m'].groupby('time.year').mean()


# In[45]:


hot = temp_yearly.mean(['longitude','latitude'])
hot['year'][hot.argmax()].values


# ```{note}
# Since we grouped by **year**, the time interval dimension was renamed to `year`.
# ```

# Alternatively, we could use the `resample` function. 

# In[46]:


temp_yearly = xds['t2m'].resample(time="Y").mean()


# In[47]:


hot = temp_yearly.mean(['longitude','latitude'])
hot['time'][hot.argmax()].values

