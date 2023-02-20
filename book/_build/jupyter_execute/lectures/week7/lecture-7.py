#!/usr/bin/env python
# coding: utf-8

# # Data access
# 
# Finding, downloading, and cleaning data is an important, but laborious, part of geospatial data science. In this demo, we will download data programmatically using Application Programming Interfaces (APIs). We will also talk about strategies to download data when an API is unavailable or insufficient.

# ## APIs
# 
# So far in this course we have mainly been using data that has been downloaded **locally** from point-and-click GUIs. But it is becoming more and more common to access data programmatically from an online server. These platforms often have a **public API** that we can use to pull data inside our Python environment. 
# 
# An API is a type of **software** that provides a **standard set of protocols/functions** so that our computer can **communicate** with other computers (in contrast, a **user interface** is a type of software that connects a **computer** to a **person**)
# 
# The basic idea is we send a **request** (which may include query parameters and access credentials) to an endpoint. That endpoint will return a **response** code plus the data we asked for. For these kind of tasks, we have to carefully inspect the API **documentation** to understand what functions are available and what keyword arguments they require.
# 
# Many organizations have great APIs because they want people to use their data.

# ## Census Bureau
# 
# The US Census Bureau has a great API that makes demographic, socio-economic and housing statistics more accessible than ever before. 
# 
# Developers use customize these statistics to create apps that:
# 
# * Provide a local government a range of socioeconomic statistics on its population.
# 
# * Show commuting patterns for every city in America.
# 
# * Display the latest numbers on owners and renters in a neighborhood someone may want to live in.
# 
# Many students will use Census Bureau data in their final projects. 

# ## `CenPy`
# 
# `CenPy` is an interface to explore and query the US Census API in **Python**. It conveniently returns the data in **`Pandas` Dataframes** for further analysis. 
# 
# We know `CenPy` is legitimate because it has an **active GitHub repository**. 
# 
# ```{image} images/cenpy-github.png
# :width: 900px
# :align: center
# ```
# 
# More information about this package can be found [here](https://github.com/cenpy-devs/cenpy).
# 
# First we should find how to install it, either using `conda` or `pip` depending on which virtual environment manager (`conda` or `venv`) we are using. 
# 
# ```{image} images/cenpy-install.png
# :width: 600px
# :align: center
# ```

# In[ ]:


# Import library
from cenpy import products
import matplotlib.pyplot as plt


# Then search the documentation for examples...
# 
# ```{image} images/cenpy-examples.png
# :width: 600px
# :align: center
# ```

# In[12]:


acs = products.ACS(2019)
acs


# In[13]:


# Find tables containing keyword
acs.filter_tables('POPULATION', by='description')


# In[14]:


# Print list of tables
acs.filter_variables('B01003')


# ```{image} images/census-geo.png
# :width: 700px
# :align: center
# ```

# In[15]:


# Download data
lane_pop = products.ACS(2019).from_county('Lane County, OR', 
                                          level='tract',
                                          variables=['B01003_001E']) # don't worry about the deprecation message!


# In[18]:


lane_pop.head()


# In[19]:


# Compute population density
lane_pop['pop_density'] = lane_pop['B01003_001E'] / (lane_pop['geometry'].area / 1e+6)

from mpl_toolkits.axes_grid1 import make_axes_locatable

# Plot map
f, ax = plt.subplots(1, 1, figsize=(10,10))

# These two lines make the colorbar the same size as the axes.
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)

lane_pop.plot('pop_density', ax=ax, legend=True, cax=cax)


# ## USGS hydrologic data
# 
# Let's have a look at another API called [`dataretrieval`](https://github.com/DOI-USGS/dataretrieval-python) which was developed by USGS to retrieve hydrologic data.
# 
# ```{image} images/usgs-github.png
# :width: 900px
# :align: center
# ```
# 
# On the GitHub `REAMDE.md` for this package it says we can also install `dataretrieval` using `conda` or `pip`.
# 
# 
# ```{image} images/usgs-install.png
# :width: 600px
# :align: center
# ```

# In[22]:


get_ipython().run_cell_magic('capture', '', '# Install package\n!pip install -U dataretrieval')


# Now we can look through the documentation and test some examples

# In[24]:


# Import the functions for downloading data from NWIS
import dataretrieval.nwis as nwis

# Specify the USGS site code
site = '03339000'

# Get instantaneous values (iv)
df = nwis.get_record(sites=site, service='dv', start='2020-10-01', end='2021-09-30')
df.head()


# In[27]:


# Plot
f, ax = plt.subplots(1, 1, figsize=(10,4))
ax.plot(df['00060_Mean'])


# ## Tips for APIs
# 
# * Take a minute to make sure that package is used (e.g. lots of forks, stars) and up-to-date (e.g. last commit)
# 
# 
# * Read the `docs`, `demos`, `examples` and hope we find what we're looking for (sometimes they are not that comprehensive)
# 
# 
# * If you can't find what you're looking for, inspect the source code (`.py` files)

# ## API limits
# 
# Often APIs are sometimes not available or have limitations. Technology companies **hoard data** to secure market dominance. But this is a problem because, by guarding data, they are also preventing it **being used** for good causes. Without access to their data it is difficult to tell whether they are in **compliance**. 
# 
# ```{image} images/zillow.png
# :width: 900px
# :align: center
# ```
# 
# 
# 
# ```{image} images/zillow2.png
# :width: 900px
# :align: center
# ```
# 
# 
# 
# ```{image} images/airbnb.png
# :width: 900px
# :align: center
# ```
# 

# ## Web scraping
# 
# 
# * Since web pages are usually organized in a specfic way, we can still download data from them. 
# 
# 
# * Web scraping (also known as crawling or harvesting) is the practice of **automatically** gathering data from the internet without the use of an **API**
# 
# 
# * Most commonly accomplished by writing a program that **queries** a web server, **requests** data (usually in the form of HTML), and **parses** that data to extract information

# ```{image} images/scrape_hero.png
# :width: 900px
# :align: center
# ```

# ```{image} images/inside_airbnb.png
# :width: 900px
# :align: center
# ```

# ## Suppose a friend wanted to do this?
# 
# * `requests`: standard Python library for requesting data from the web
# 
# 
# * `BeautifulSoup`: a library for pulling data out of HTML and XML files
# 
# 
# * `selenium`: is a library for performing **web browser automation**

# ### `requests`
# 
# A lot of data on Wikipedia is contained in HTML tables which have the following syntax.
# 
# 
# * The table itself starts with the `<table>` tag and finishes with `</table>`
# 
# 
# * Table rows start with the `<tr>` tag and finish with `</tr>`
# 
# 
# * Table headers start with the `<th>` tag and finish with `</th>`
# 
# 
# * Table data start with the `<td>` tag and finish with `</td>`
# 
# 
# The table below, showing some of the biggest soccer clubs in the world, is an example of a simple HTML table. 

# <table>
#   <tr>
#     <th>Team</th>
#     <th>Manager</th>
#     <th>Country</th>
#   </tr>
#   <tr>
#     <td>Real Madrid</td>
#     <td>Carlo Ancelotti</td>
#     <td>Spain</td>
#   </tr>
#   <tr>
#     <td>Bayern Munich</td>
#     <td>Julian Nagelsmann</td>
#     <td>Germany</td>
#   </tr>
#     <tr>
#     <td>Hull City</td>
#     <td>Liam Rosenior</td>
#     <td>England</td>
#   </tr>
#     <tr>
#     <td>Paris Saint-Germain</td>
#     <td>Christophe Galtier</td>
#     <td>France</td>
#   </tr>
# </table>

# ```{image} images/html.png
# :width: 300px
# :align: center
# ```

# In[28]:


# Import packages
import requests

# Open a webpage
html = requests.get('https://en.wikipedia.org/wiki/Climate_of_Oregon')

# HTML
html


# ```{image} images/climate_wiki.png
# :width: 900px
# :align: center
# ```

# ```{image} images/more_html.png
# :width: 900px
# :align: center
# ```

# ## BeautifulSoup4
# 
# * Now we could write a program to **parse** this HTML code (i.e. split into useful blocks)... 
# 
# 
# * ...or we could use another package called `BeautifulSoup` (also known as `bs4`) a Python library for parsing data out of HTML and XML files
# 
# ```{image} images/bs4.jpg
# :width: 200px
# :align: center
# ```
# 

# In[42]:


# Import package
from bs4 import BeautifulSoup, SoupStrainer

# Read HTML content as "soup object" and define default parser
soup = BeautifulSoup(html.text, 'html.parser')


# ### Parse HTML
# 
# The `.find` and `.find_all` are the most common methods we will use. They can be used to filter HTML code to find a list of tags or tags with specific attributes.  

# In[43]:


# Define heading tags
heading_tags = ["h1", "h2"]

# Find heading tags in HTML code
headings = soup.find_all(heading_tags)

# Loop over every heading and print text
for tags in headings:
    print(tags.name + ' -> ' + tags.text.strip())


# In[44]:


# Find every hyperlink
links = soup.find_all('a')

# Loop over every link and print hyperlink
for link in links[0:10]:
    print(link.get('href'))


# In[45]:


# Find number of images on page
len(soup.find_all('img'))


# In[51]:


# Print details of first image
print(soup.find_all('img')[5])


# In[52]:


# Find attributes of first image
print(soup.find_all('img')[5].attrs['src'])


# In[53]:


# Download image
url = 'https://' + soup.find_all('img')[5].attrs['src'][2:]
response = requests.get(url)
if response.status_code == 200:
    with open("images/test_image.jpg", 'wb') as f:
        f.write(response.content)


# In[54]:


# Import packages
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Read image
img = mpimg.imread('images/test_image.jpg')

# Plot image
plt.imshow(img)


# ## Selenium
# 
# * Sometimes we want even more control...
# 
# 
# * Selenium is a package for performing **web browser automation**
# 
# 
# * We can use Selenium to enter text in search boxes, click buttons etc. 
# 
# 
# ```{image} images/selenium.png
# :width: 200px
# :align: center
# ```

# In[56]:


get_ipython().run_cell_magic('capture', '', '# Install webdriver_manager: https://github.com/SergeyPirogov/webdriver_manager\n!pip3 install webdriver_manager')


# In[57]:


# Import packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# In[58]:


# Install Chrome webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open a web browser at the following page
driver.get("https://www.google.com/maps")


# ```{image} images/google_maps.png
# :width: 900px
# :align: center
# ```

# ```{image} images/inspect.png
# :width: 900px
# :align: center
# ```
# 

# In[4]:


# Enter some text in the search box
inputElement = driver.find_element(By.ID, "searchboxinput")
inputElement.send_keys('South Sister Oregon')


# ```{image} images/enter_text.png
# :width: 900px
# :align: center
# ```
# 

# In[5]:


# Click search button
element = driver.find_element(By.ID, "searchbox-searchbutton")
element.click()


# ```{image} images/search.png
# :width: 900px
# :align: center
# ```
# 
