#!/usr/bin/env python
# coding: utf-8

# # Maps with data
# 
# In the second part of this lecture, we will use Python to produce another type of thematic map. But this instead of representing elevation data, we will visualize Census Bureau data.
# 
# We can automatically download Census Bureau data from the 2019 American Community Survey using `CenPy`. 

# In[1]:


from cenpy import products
acs = products.ACS(2019)


# ## Search for data
# 
# Inspired by the article "[Plumbing Poverty: Mapping Hot Spots of Racial and Geographic Inequality in U.S. Household Water Insecurity](https://www.tandfonline.com/doi/abs/10.1080/24694452.2018.1530587)" by Shiloh Deitz and Katie Meehan (2019), we will search for data that determines whether household have adequate plumbing facilities. 
# 
# The Census Bureau defines "complete plumbing facilities" as (1) piped hot and cold water, (2) a flush toilet, and (3) a bathtub or shower, all located within the housing unit and used only by occupants. We can find the variable **code** in the data tables by searching for the word "**plumbing**".

# In[ ]:


acs.filter_tables('PLUMBING', by='description')


# In[ ]:


# Print list of tables
acs.filter_variables('B25047')


# ## Download data
# 
# We will focus our analysis on western United States and download data at the **county** level. Of course, a more local analysis could look at smaller spatial scales such as the tract or block group level. 

# In[ ]:


# Download data
wa_plumbing = products.ACS(2019).from_state('Washington', 
                                          level='county',
                                          variables=['B25047_001E', 'B25047_002E', 'B25047_003E'])
or_plumbing = products.ACS(2019).from_state('Oregon', 
                                          level='county',
                                          variables=['B25047_001E', 'B25047_002E', 'B25047_003E'])
ca_plumbing = products.ACS(2019).from_state('California', 
                                          level='county',
                                          variables=['B25047_001E', 'B25047_002E', 'B25047_003E'])
az_plumbing = products.ACS(2019).from_state('Arizona', 
                                          level='county',
                                          variables=['B25047_001E', 'B25047_002E', 'B25047_003E'])
nm_plumbing = products.ACS(2019).from_state('New Mexico', 
                                          level='county',
                                          variables=['B25047_001E', 'B25047_002E', 'B25047_003E'])
id_plumbing = products.ACS(2019).from_state('Idaho', 
                                          level='county',
                                          variables=['B25047_001E', 'B25047_002E', 'B25047_003E'])
az_plumbing = products.ACS(2019).from_state('Arizona', 
                                          level='county',
                                          variables=['B25047_001E', 'B25047_002E', 'B25047_003E'])
ut_plumbing = products.ACS(2019).from_state('Utah', 
                                          level='county',
                                          variables=['B25047_001E', 'B25047_002E', 'B25047_003E'])
id_plumbing = products.ACS(2019).from_state('Idaho', 
                                          level='county',
                                          variables=['B25047_001E', 'B25047_002E', 'B25047_003E'])
nv_plumbing = products.ACS(2019).from_state('Nevada', 
                                          level='county',
                                          variables=['B25047_001E', 'B25047_002E', 'B25047_003E'])


# In[ ]:


wa_plumbing.head()


# In[ ]:


plumbing = pd.concat([wa_plumbing, or_plumbing, ca_plumbing, 
                      az_plumbing, ut_plumbing, id_plumbing, 
                      nv_plumbing])

# Compute proportion of household with inadequate plumbing
plumbing['lack_plumbing_percent'] = plumbing['B25047_003E'] / plumbing['B25047_001E']


# ## Simple choropleth map
# 
# `GeoPandas` provides a high-level interface to the `Matplotlib` library for making maps. It is as easy as using the `plot()` method on a `GeoDataFrame`. 

# In[ ]:


plumbing.plot('lack_plumbing_percent')


# ## Improving the choropleth map
# 
# This is useful for a quick look over the data but we would prefer to customize our plot. For instance, we should add a title, colorbar, and nicer colormap. 

# In[ ]:


fig, ax = plt.subplots(figsize=(8,5))

plt.title('Lack of plumbing in the western United States', fontsize=10)
ax.set_axis_off()
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="3%", pad=0.5,alpha=0.5)
plumbing.plot('lack_plumbing_percent', ax=ax, alpha=0.5, cmap='Greens', 
              edgecolor='k', legend=True, cax=cax, linewidth=0.1)
plt.ylabel('Proportion of households', fontsize=10)
plt.show()


# ## Interactive plots
# 
# Alongside static plots, `GeoPandas` can produce [interactive maps](https://geopandas.org/en/stable/docs/user_guide/interactive_mapping.html) based on the [`Folium`](https://github.com/python-visualization/folium) library, which is itself based on [`Leaflet`](https://leafletjs.com/). 

# In[ ]:


m = plumbing.explore(
     column="lack_plumbing_percent", # make choropleth based on column
     scheme="naturalbreaks",         # use mapclassify's natural breaks scheme
     tooltip="lack_plumbing_percent",# show column value in tooltip (on hover)
     popup=True,                     # show all values in popup (on click)
     tiles="CartoDB positron",       # use "CartoDB positron" tiles
     cmap="Greens",                  # use "Greens" matplotlib colormap
     style_kwds=dict(color="black", weight=0.5) # use black outline with weight of 1
    )
m


# ## Conclusions
# 
# Maps made using programming don't have to be terrible - it is possible to produce visually appealing maps in Python. They may never be quite as good as what professional cartographers can produce in Adobe Illustrator but they have other advantages. Once the code is written, we can quickly make edits or add another dataset. I hope this demo has inspired you to improve the quality of your Python plots! 

# Content in this lecture was inspired by [Adam Symington](https://www.pythonmaps.com/) and this [tutorial](https://towardsdatascience.com/creating-beautiful-topography-maps-with-python-efced5507aa3). 
