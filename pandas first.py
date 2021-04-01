#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd


# In[8]:


df = pd.read_csv('data/survey_results_public.csv') #to load a file in jupyter notebook


# In[31]:


df  #to print loaded data


# In[37]:


df.head(10) #to check desired number of rows in data if we want to see from the top
df.tail(10) #to check desired number of rows in data if we want to see from the bottom


# In[19]:


df.shape #to check number of rows and column


# In[6]:


df.info() #to check data type of table


# In[28]:


pd.set_option('display.max_column',85) #to set to see all the column in the data
pd.set_option('display.max_rows',85)  #to set to see all the rows in the data


# In[25]:


schema_df = pd.read_csv('data/survey_results_schema.csv') #give column/schema in our data


# In[30]:


schema_df #to read the data of schema


# In[1]:


pass


# In[2]:


pass


# In[ ]:




