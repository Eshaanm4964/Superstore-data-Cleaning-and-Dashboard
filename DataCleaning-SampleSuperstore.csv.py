#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


# In[35]:


data = pd.read_csv("SampleSuperstore.csv", encoding='latin1')


# In[36]:


data.head()


# In[37]:


data.isnull()


# In[38]:


data.isnull().sum()


# In[39]:


data.info()


# In[40]:


data.describe()


# In[41]:


data.tail()


# In[42]:


data.columns.tolist()


# In[43]:


data.drop(columns = "Row ID",axis = 1)


# In[44]:


data.to_string()


# In[45]:


data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Ship Date'] = pd.to_datetime(data['Ship Date'])


# In[22]:


data.head(10)


# In[46]:


data['Profit Margin'] = (data['Profit'] / data['Sales']).round(2)
data['Order Processing Time'] = (data['Ship Date'] - data['Order Date']).dt.days


# In[47]:


data.head()


# In[48]:


data.rename(columns={'Sub-Category': 'SubCategory', 'Customer Name': 'CustomerName'}, inplace=True)


# In[49]:


data.head(10)


# In[51]:


data.columns.to_list()


# In[52]:


data = data[data['Sales'] > 0]
data = data[data['Profit'].notnull()]


# In[53]:


data.head()


# In[55]:


data.to_csv('Cleaned_Superstore_Data.csv', index=False)


# In[61]:


get_ipython().system('pip install IPython')


# In[64]:


from IPython.display import FileLink
FileLink("Cleaned_Superstore_Data.csv")


# In[ ]:




