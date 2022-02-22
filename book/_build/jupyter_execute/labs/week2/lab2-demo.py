#!/usr/bin/env python
# coding: utf-8

# # Exploring vector data
# 
# **Objectives:**
#    * Explore a large wildfire dataset using `pandas` and `geopandas`.
#    * Query `pandas DataFrames` and find descriptive statistics
#    * Filter and aggregate `pandas DataFrames`
#    * Plot time-series data

# ### Check for any updates in course materials
# 
# Before we start this assignment, we need to check whether there are any updates to the original course repository. We can do this by adding the original repository (the one we forked) as a *remote*. Command line users can do this by running:
# 
# <code>git remote add upstream https://github.com/JohnnyRyan1/geospatial-data-science</code>
# 
# Then fetch and merge the updated course content by running:
# 
# <code>git fetch upstream</code>
# 
# <code>git merge upstream/master master</code>
# 
# GitHub Desktop users should first click the **Fetch origin** button to check for new changes. Then click the triangle symbol next to **Current branch: master**, click **Choose a branch to merge into master**, click **upstream/master** from **Other branches** and click **Create a merge commit**. 
# 
# Any new updates to the course repository will now be available in your local repository.

# ### Create a new environment and launch the notebook
# 
# There is an `environment.yml` file in each lab folder. This file contains a list of packages required for completing the assignments. The `environment.yml` file in this lab, for example, includes the `geopandas` package that is really useful for reading, analyzing, and writing vector data.  
# 
# We can install this environment using the instructions in Lab 1 but we will repeat them here as well. Navigate to the `labs/lab2` folder (either from the terminal for Linux and Mac users or from the **CMD.exe Prompt** launched from **Anaconda Navigator** for Windows users) and run:
# 
# `conda env create -f environment.yml`
# 
# Activate this environment by running:
# 
# `conda activate lab2`
# 
# Now launch the notebook by running:
# 
# `jupyter notebook 02_wildfires_in_lane_county.ipynb`

# ### Download the data for the lab
# 
# We will be using a wildfire dataset for 1992-2018 period compiled from US federal, state, and local reporting systems by the Forest Service. More info can be found here: https://www.fs.usda.gov/rds/archive/Catalog/RDS-2013-0009.5. Since the max file size for GitHub is 2 GB, the lab data will be available on Dropbox. See Slack (or Canvas) for the Dropbox link. 
# 
# Once you have launched the notebook and downloaded the data, we are ready to begin...

# In[3]:


# Import modules
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


# In[4]:


# Define data filepath
pathname = '/Users/jryan4/Dropbox (University of Oregon)/Teaching/geospatial-data-science/data/lab2/'

# Read data
df = gpd.read_file(pathname + 'or_1992-2018.shp') # 'df' stands for DataFrame


# ### Some basic querying

# In[12]:


# Find column labels
df.columns


# **Note** that the max length of a shapefile column header is **10 characters**. A full list of columns can be found below:
# 
# ### Column labels
# 
# 
# FOD_ID = Unique numeric record identifier.
# 
# FPA_ID = Unique identifier that contains information necessary to track back to the original record in the source dataset.
# 
# SOURCE_SYSTEM_TYPE = Type of source database or system that the record was drawn from (federal, nonfederal, or interagency).
# 
# SOURCE_SYSTEM = Name of or other identifier for source database or system that the record was drawn from. See Table 1 in Short (2014), or \Supplements\FPA_FOD_source_list.pdf, for a list of sources and their identifier.
# 
# NWCG_REPORTING_AGENCY = Active National Wildlife Coordinating Group (NWCG) Unit Identifier for the agency preparing the fire report (BIA = Bureau of Indian Affairs, BLM = Bureau of Land Management, BOR = Bureau of Reclamation, DOD = Department of Defense, DOE = Department of Energy, FS = Forest Service, FWS = Fish and Wildlife Service, IA = Interagency Organization, NPS = National Park Service, ST/C&L = State, County, or Local Organization, and TRIBE = Tribal Organization).
# 
# NWCG_REPORTING_UNIT_ID = Active NWCG Unit Identifier for the unit preparing the fire report.
# 
# NWCG_REPORTING_UNIT_NAME = Active NWCG Unit Name for the unit preparing the fire report.
# 
# SOURCE_REPORTING_UNIT = Code for the agency unit preparing the fire report, based on code/name in the source dataset.
# 
# SOURCE_REPORTING_UNIT_NAME = Name of reporting agency unit preparing the fire report, based on code/name in the source dataset.
# 
# LOCAL_FIRE_REPORT_ID = Number or code that uniquely identifies an incident report for a particular reporting unit and a particular calendar year.
# 
# LOCAL_INCIDENT_ID = Number or code that uniquely identifies an incident for a particular local fire management organization within a particular calendar year.
# 
# FIRE_CODE = Code used within the interagency wildland fire community to track and compile cost information for emergency fire suppression (https://www.firecode.gov/).
# 
# FIRE_NAME = Name of the incident, from the fire report (primary) or ICS-209 report (secondary).
# 
# ICS_209_PLUS_INCIDENT_JOIN_ID = Primary identifier needed to join into operational situation reporting data for the incident in the ICS-209-PLUS dataset.
# 
# ICS_209_PLUS_COMPLEX_JOIN_ID = If part of a complex, secondary identifier potentially needed to join to operational situation reporting data for the incident in the ICS-209-PLUS dataset (2014 and later only).
# 
# MTBS_ID = Incident identifier, from the MTBS perimeter dataset.
# 
# MTBS_FIRE_NAME = Name of the incident, from the MTBS perimeter dataset.
# 
# COMPLEX_NAME = Name of the complex under which the fire was ultimately managed, when discernible.
# 
# FIRE_YEAR = Calendar year in which the fire was discovered or confirmed to exist.
# 
# DISCOVERY_DATE = Date on which the fire was discovered or confirmed to exist.
# 
# DISCOVERY_DOY = Day of year on which the fire was discovered or confirmed to exist.
# 
# DISCOVERY_TIME = Time of day that the fire was discovered or confirmed to exist.
# 
# NWCG_CAUSE_CLASSIFICATION = Broad classification of the reason the fire occurred (Human, Natural, Missing data/not specified/undetermined).
# 
# NWCG_GENERAL_CAUSE = Event or circumstance that started a fire or set the stage for its occurrence (Arson/incendiarism, Debris and open burning, Equipment and vehicle use, Firearms and explosives use, Fireworks, Misuse of fire by a minor, Natural, Power generation/transmission/distribution, Railroad operations and maintenance, Recreation and ceremony, Smoking, Other causes, Missing data/not specified/undetermined).
# 
# NWCG_CAUSE_AGE_CATEGORY = If cause attributed to children (ages 0-12) or adolescents (13-17), the value for this data element is set to Minor; otherwise null.
# 
# CONT_DATE = Date on which the fire was declared contained or otherwise controlled (mm/dd/yyyy where mm=month, dd=day, and yyyy=year).
# 
# CONT_DOY = Day of year on which the fire was declared contained or otherwise controlled.
# 
# CONT_TIME = Time of day that the fire was declared contained or otherwise controlled (hhmm where hh=hour, mm=minutes).
# 
# FIRE_SIZE = The estimate of acres within the final perimeter of the fire.
# 
# FIRE_SIZE_CLASS = Code for fire size based on the number of acres within the final fire perimeter (A=greater than 0 but less than or equal to 0.25 acres, B=0.26-9.9 acres, C=10.0-99.9 acres, D=100-299 acres, E=300 to 999 acres, F=1000 to 4999 acres, and G=5000+ acres).
# 
# LATITUDE = Latitude (NAD83) for point location of the fire (decimal degrees).
# 
# LONGITUDE = Longitude (NAD83) for point location of the fire (decimal degrees).
# 
# OWNER_DESCR = Name of primary owner or entity responsible for managing the land at the point of origin of the fire at the time of the incident.
# 
# STATE = Two-letter alphabetic code for the state in which the fire burned (or originated), based on the nominal designation in the fire report.
# 
# COUNTY = County, or equivalent, in which the fire burned (or originated), based on nominal designation in the fire report.
# 
# FIPS_CODE = Five-digit code from the Federal Information Process Standards (FIPS) publication 6-4 for representation of counties and equivalent entities, based on the nominal designation in the fire report.
# 
# FIPS_NAME = County name from the FIPS publication 6-4 for representation of counties and equivalent entities, based on the nominal designation in the fire report.

# In[13]:


# Find columns datatypes
df.dtypes


# In[14]:


# Get some stats for numeric columns
df['FIRE_SIZE'].describe()


# So it appears that most fires are extremely small (i.e. 75% of wildfire are less than 0.33 acres)

# ### Apply filters

# In[15]:


# Filter fires larger than 100 acres
df_large = df[df['FIRE_SIZE'] > 100]


# In[16]:


# Find mean size of wildfires larger than 100 acres
df_large['FIRE_SIZE'].mean()


# In[17]:


# Find the different cause of large wildfires
df_large['NWCG_CAUSE'].unique()


# In[18]:


# Filter fires that were caused by natural causes
df_large_natural = df_large[df_large['NWCG_CAUSE'] == 'Natural'].copy()


# ### `datetime` functionality

# In[19]:


# Find date of discovery
df_large_natural['DISCOVERY_']


# `pandas` contains extensive capabilities and features for working with time series data. But to access this functionality, we need to convert the datatype of this column from `object` to `datetime64`. 

# In[20]:


datetime = pd.to_datetime(df_large_natural['DISCOVERY_'], format='%Y/%m/%d %H:%M:%S.%f')
datetime


# In[21]:


df_large_natural['datetime'] = datetime


# In[22]:


# Filter large, natural wildfires in 2016
df_large_natural_2016 = df_large_natural[df_large_natural['datetime'].dt.year == 2016]


# ### Group by categories

# In[23]:


# Find number of large fires in each year (i.e. number of rows in each year)
large_fire_count = df_large.iloc[:,0].groupby(df_large_natural['datetime'].dt.year).count()


# In[24]:


# Find acres of wildfire for each year
large_fire_area = df_large['FIRE_SIZE'].groupby(df_large_natural['datetime'].dt.year).sum()


# ### Plot

# In[25]:


# Plot number and acres of wildfire for each year
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(10,8), sharex=True)
ax1.plot(large_fire_count, lw=2)
ax1.set_ylabel('Number of fires (>100 acres)', fontsize=14)
ax1.tick_params(axis='x', labelsize=14)
ax1.tick_params(axis='y', labelsize=14)
ax1.grid(ls='dotted', lw=2, alpha=0.5)

ax2.plot(large_fire_area, lw=2)
ax2.set_ylabel('Area of fires (>100 acres)', fontsize=14)
ax2.tick_params(axis='x', labelsize=14)
ax2.tick_params(axis='y', labelsize=14)
ax2.grid(ls='dotted', lw=2, alpha=0.5)


# *********
# 
# ## Question 1 (20 points): 
# 
# Make a **new file** (either a Jupyter Notebook or Spyder `.py` file) and name it `lab2_submission.ipynb`. Write some code to answer the following questions:
# 
# * a) Which **county** had the most **human** caused wildfires **>50 acres**? (HINT: use the `FIPS_NAME` column)
# * b) Which **month** had the most **natural** caused wildfires **>100 acres**?
# * c) How many fires **>200 acres** have an **undetermined** cause (e.g. `Missing data/not specified/undetermined`?
# * d) What is the name, date, and county of the **largest sized fire**?
# * e) How many wildfires in **Lane County** were **>50 acres**?
# 
# *Remember, focus on adapting the example code rather than writing your own from scratch.*
# **************

# ## Lab 2b: Where are wildfires occurring in Lane County Oregon?
# 
# So we have established that there were some fires in Lane County between 1992 and 2018. But what if we wanted to know more about where they were and how many people might have been affected? We can do this using Census Bureau data which provides population estimates at relatively small spatial scales. 
# 
# **Objectives:**
#    * Introduce Census Bureau data data variables and geographic units using <code>cenpy</code>.
#    * Compute how many people were impacted by wildfires in Lane County, Oregon using just a few lines of code
#    * Calculate some statistics using the <code>pandas</code> library
#    * Produce a chloropleth map
# 
# We will be relying heavily on <code>cenpy</code> which is a package that enables automatic discovery and download of US Census Bureau data. <code>cenpy</code> formats Census data as a <code>geopandas</code> DataFrame for analysis in Python or export to GIS software such as QGIS. More information about this package can be found [here](https://nbviewer.org/github/ljwolf/cenpy/blob/master/notebooks/product-api.ipynb?flush_cache=true), [here](https://nbviewer.org/github/cenpy-devs/cenpy/blob/master/notebooks/segregation.ipynb), and the [GitHub repo](https://github.com/cenpy-devs/cenpy).

# ### Query Census data variables
# 
# To download data, we first need to identify the relevant product and variables of interest to us. We will use data from the American Community Survey (ACS) product which provides social and economic information every year but, unlike the Decenniel Survey, only represents a sample (about 3.5 million) of US households. 

# In[26]:


# Import modules
from cenpy import products
import matplotlib.pyplot as plt

# Define product
acs = products.ACS(2019)


# Now we need a list of Census variables. One way to do this is to browse the ACS documentation which can be found here: https://api.census.gov/data/2019/acs/acs5/variables.html. The other is to search the tables using keywords and <code>cenpy</code>.

# In[27]:


# Print list of tables
acs.filter_tables('POPULATION', by='description')


# In[28]:


# Print list of variables
acs.filter_variables('B01003')


# ### Census data geographic units
# 
# So it looks like the variable **B01003_001E** contains population data. For the purposes of demonstration, we will now download this data at the **tract level** which is the third smallest geographic unit in Census data. In another lab we will use smaller geographic units.

# <div>
# <img src="images/census_geographic_units.png" width="800"/>
# </div>

# ### Download Census data and compute statistics

# In[29]:


# Download data
lane_pop = products.ACS(2019).from_county('Lane County, OR', level='tract',
                                        variables=['B01003_001E']) # don't worry about the deprecation message!


# Now let’s look at some summary statistics.

# In[30]:


# Calculate some stats
lane_pop['B01003_001E'].describe()


# This shows that there are 87 tracts in Lane County with a mean population of 4,291 people. Some tracts have 0 people while one has 8,932.

# ### Plot
# 
# We can plot tract population easily.

# In[31]:


# Plot map
f, ax = plt.subplots(1, 1, figsize=(10,10))
lane_pop.plot('B01003_001E', ax=ax, cmap='plasma')


# A more useful metric might be population density (i.e. people per km<sup>2</sup>)

# In[32]:


lane_pop['pop_density'] = lane_pop['B01003_001E'] / (lane_pop['geometry'].area / 1e+6)

from mpl_toolkits.axes_grid1 import make_axes_locatable

# Plot map
f, ax = plt.subplots(1, 1, figsize=(10,10))

# These two lines make the colorbar the same size as the axes.
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)

lane_pop.plot('pop_density', ax=ax, cmap='plasma', legend=True, cax=cax)


# ### Locate the wildfires
# 
# If we want to locate the wildfires we have to ensure that both the GeoDataFrames (the wildfire and population dataset) are in the same coordinate system.

# In[33]:


lane_pop.crs


# In[34]:


# Make 
df_large = df[df['FIRE_SIZE'] > 100]
lane_fires = df_large[df_large['FIPS_NAME'] == 'Lane County']
lane_fires.crs


# So it looks like the wildfire dataset has **WGS84 geographic coordinate system** while the Census data has a **Pseudo-Mercator projected coordinate system**. We can convert the wildfire dataset easily.

# In[35]:


lane_fires_proj = lane_fires.to_crs('EPSG:3857')
lane_fires_proj.crs


# In[36]:


# Plot map
f, ax = plt.subplots(1, 1, figsize=(10,10))

# These two lines make the colorbar the same size as the axes.
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)

lane_pop.plot('pop_density', ax=ax, cmap='plasma', legend=True, cax=cax)
lane_fires_proj.plot(ax=ax, c='red')


# So it looks like most fairly large fires in Lane County were not too close to Eugene. We can find out how many fires were in each tract using a spatial join (`gpd.sjoin`) and a little bit of wrangling (`.groupby`) to count the number of occurrences. 

# In[37]:


# Spatial join
joined_df = gpd.sjoin(lane_fires_proj, lane_pop, how='inner', predicate='intersects')

# Groupby tract
tract_count = joined_df.groupby(['tract'], as_index=False)['OBJECTID'].count()
tract_count.columns = ['tract', 'fire_count']

# Merge back to original DataFrame
merged_df = lane_pop.merge(tract_count, on='tract', how='left')

# Clean up data by filling NaNs with 0
merged_df['fire_count'].fillna(0, inplace=True)  

# Plot map
f, ax = plt.subplots(1, 1, figsize=(10,10))
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)
merged_df.plot('fire_count', ax=ax, cmap='plasma', legend=True, cax=cax)


# I hope this lab provided some insight into the ridiculous power of `geopandas` for handling geospatial vector data (both points and polygons). 

# *********
# 
# ## Question 2 (20 points): 
# * a) Write some more code in `lab2_submission.ipynb` to produce a chloropleth map for a city, county or state showing a Census variable (or derived variable) of your choice. Consider choosing a place or variable that inetrests you. The following is a useful guide: https://nbviewer.org/github/ljwolf/cenpy/blob/master/notebooks/product-api.ipynb?flush_cache=true
# 
# Note that:
# * If your map represents a state, use county level data
# * If your map represents a county or city, use tract level data
# 
# The following table provides a list of Census variables: https://api.census.gov/data/2019/acs/acs5/variables.html
# 
# ## Task 3 (10 points):
# * a) Save your answers notebook, commit and push to GitHub using instructions from Lab 1
# * c) Also upload your answers as a <code>.pdf</code> to Canvas
# 
# **************

# ## Remember to submit your answers to Questions 1 and 2 and Task 3 **by Friday 11:59pm**

# In[ ]:




