#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install census')
get_ipython().system('pip install us')


# In[20]:


get_ipython().system('pip install openpyxl')


# In[1]:


from census import Census
from us import states
import pandas as pd


# In[2]:


c = Census("5f7e25f1ce5f52828e64cc4e5ff5f470759b4e03")


# In[4]:


codes = ['B19301_001E', 'B01003_001E']


# In[52]:


data = c.acs5.state_county_tract((codes), states.OR.fips, '039', Census.ALL)


# In[53]:


df = pd.DataFrame(data)


# In[54]:


df.dtypes


# In[55]:


df.to_csv('/Users/jryan4/Dropbox (University of Oregon)/teaching/gds-applications-site/book/activities/week2/data/census.csv', index=False)


# In[ ]:




