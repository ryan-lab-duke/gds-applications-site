#!/usr/bin/env python
# coding: utf-8

# # Data access lecture

# <CENTER>
#     <h1> Geospatial Data Science Applications: GEOG 4/590</h1>
#     <h3>Feb 14, 2022</h3>
#     <h2>Lecture 7: Data access</h2>
#     <img src="images/coding-computer-programming.jpeg" width="300"/>
#     <h3>Johnny Ryan: jryan4@uoregon.edu</h3>
# </CENTER>

# ## Content of this lecture
# 
# * Web2.0
# <br>
# <br>
# * Standard data access using APIs
# <br>
# <br>
# * What to do when an API is unavailable or insufficient?
# <br>
# <br>
# * Background for this week's lab

# In[1]:


from IPython.display import HTML
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/BxV14h0kFs0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')


# ## APIs
# 
# 
# * Application programming interface
# 
# 
# * A type of **software** that provides a **standard set of protocols/functions** so that our computer can **communicate** with other computers
# 
# 
# * In contrast, a **user interface** is a type of software that connects a **computer** to a **person**

# ## APIs
# 
# * Many organizations have great APIs because they want people to use their data
# 
# 
# * We have used one...

# * `cenpy`

# <img src="images/usgs.png" width="1000"/>

# In[2]:


# Install package
get_ipython().system('pip install -U dataretrieval')


# <img src="images/usgs_example.png" width="1000"/>

# In[3]:


# Import the functions for downloading data from NWIS
import dataretrieval.nwis as nwis

# Specify the USGS site code
site = '03339000'

# Get instantaneous values (iv)
df = nwis.get_record(sites=site, service='dv', start='2020-10-01', end='2021-09-30')
df


# In[4]:


# Simple plot
df['00060_Mean'].plot()


# ## Tips for APIs
# 
# * Take a minute to make sure that package is used (e.g. lots of forks, stars) and up-to-date (e.g. last commit)
# 
# 
# * Read the `docs`, `demos`, `examples` and hope we find what we're looking for (sometimes they are not that comprehensive)
# 
# 
# * If you can't find what you're looking for, inspect the source code (`.py` files)

# ## APIs are sometimes not available or have limitations

# <img src="images/zillow.png" width="1000"/>

# <img src="images/zillow2.png" width="1000"/>

# <img src="images/airbnb.png" width="1000"/>

# * These companies hoard data to secure market dominance
# 
# 
# * Without access to their data it is difficult to tell whether they are in compliance
# 
# 
# * By guarding data, they are also preventing it being used for good (maybe bad) causes 

# <img src="images/cambridge.png" width="1000"/>

# Facebook loophole that allowed third-party apps to access not only user profile data but profile data of all friends. Kogan copied someone else's idea and made "thisisyourdigitallife". Only 270K used it but collected data from all friends of users (50+ million FB profiles).

# ## Web scraping
# 
# * Also known as crawling or harvesting is the practice of **automatically** gathering data from the internet without the use of an **API**
# 
# 
# * Most commonly accomplished by writing a program that **queries** a web server, **requests** data (usually in the form of HTML), and **parses** that data to extract information

# <img src="images/scrape_hero.png" width="1000"/>

# <img src="images/inside_airbnb.png" width="1000"/>

# ## Suppose a friend wanted to do this?
# 

# * Some HTML basics
# 
# 
# * `requests`: standard Python library for requesting data from the web
# 
# 
# * `BeautifulSoup`: a library for pulling data out of HTML and XML files
# 
# 
# * `selenium`: is a library for performing **web browser automation**

# <img src="images/html.png" width="800"/>

# <html>
#     <h1>Geospatial Data Science Applications: GEOG 4/590</h1>
#     <h3>Feb 14, 2022</h3>
#     <h2>Lecture 7: Data access</h2>
#     <img src="images/coding-computer-programming.jpeg" width="150"/>
#     <h3>Johnny Ryan: jryan4@uoregon.edu</h3>
# </html>

# ### `requests`

# In[2]:


# Import packages
import requests 


# In[7]:


# Open a webpage
html = requests.get('https://en.wikipedia.org/wiki/Climate_of_Oregon')

# HTML
html


# <img src="images/climate_wiki.png" width="1000"/>

# <img src="images/more_html.png" width="1000"/>

# ## BeautifulSoup4
# 
# * Now we could write a program to **parse** this HTML code (i.e. split into useful blocks)... 
# 
# 
# * ...or we could use another package called `BeautifulSoup` (also known as `bs4`) a Python library for parsing data out of HTML and XML files
# 
# <img src="images/bs4.jpg" width="200"/>

# ### Import packages

# In[9]:


# Import package
from bs4 import BeautifulSoup, SoupStrainer


# In[20]:


# Read HTML content as "soup object" and define default parser
soup = BeautifulSoup(html.text, 'html.parser')


# ### Parse HTML using 
# 
# The `.find` and `.find_all` are the most common methods we will use. They can be used to filter HTML code to find a list of tags or tags with specific attributes.  

# In[24]:


# Define heading tags
heading_tags = ["h1", "h2"]

# Find heading tags in HTML code
headings = soup.find_all(heading_tags)

# Loop over every heading and print text
for tags in headings:
    print(tags.name + ' -> ' + tags.text.strip())


# In[31]:


# Find every hyperlink
links = soup.find_all('a')

# Loop over every link and print hyperlink
for link in links:
    print(link.get('href'))


# In[98]:


# Find number of images on page
len(soup.find_all('img'))


# In[104]:


# Print details of first image
print(soup.find_all('img')[0])


# In[103]:


# Find attributes of first image
print(soup.find_all('img')[0].attrs['src'])


# In[97]:


# Download image
url = 'https://' + soup.find_all('img')[0].attrs['src'][2:]
response = requests.get(url)
if response.status_code == 200:
    with open("images/test_image.jpg", 'wb') as f:
        f.write(response.content)


# In[99]:


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
# <img src="images/selenium.png" width="200"/>

# In[1]:


# Install webdriver_manager: https://github.com/SergeyPirogov/webdriver_manager
get_ipython().system('pip3 install webdriver_manager')


# In[2]:


# Import packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# In[3]:


# Install Chrome webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open a web browser at the following page
driver.get("https://www.google.com/maps")


# <img src="images/google_maps.png" width="1000"/>

# <img src="images/inspect.png" width="1000"/>

# In[4]:


# Enter some text in the search box
inputElement = driver.find_element(By.ID, "searchboxinput")
inputElement.send_keys('South Sister Oregon')


# <img src="images/enter_text.png" width="1000"/>

# In[5]:


# Click search button
element = driver.find_element(By.ID, "searchbox-searchbutton")
element.click()


# <img src="images/search.png" width="1000"/>
