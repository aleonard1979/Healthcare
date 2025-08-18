#!/usr/bin/env python
# coding: utf-8

# ## Health care

# In[17]:


#import needed libraries
import pandas as pd
import numpy as np
import datetime


# In[18]:


df = pd.read_csv(r'C:\Users\Antonio\Downloads\healthcare_dataset.csv')


# In[19]:


df.head()


# In[20]:


df.info()


# In[21]:


df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])
df['Discharge Date'] = pd.to_datetime(df['Discharge Date'])


# In[22]:


df.dtypes


# In[23]:


df.drop_duplicates()


# In[24]:


df['Name'] = df['Name'].str.title()


# In[25]:


name_split = df['Name'].str.split(" ", n=1,expand=True)
df['first_name'] = name_split[0]
df['last_name'] = name_split[1]


# In[26]:


df.rename(columns={'Name': 'Full_Name'}, inplace=True)


# In[27]:


df['Admission_Year'] = pd.DatetimeIndex(df['Date of Admission']).year
df['Admission_Month'] = pd.DatetimeIndex(df['Date of Admission']).month_name()


# In[28]:


df.head()


# In[31]:


df['Hospital_Stay_Length'] = df['Discharge Date'] - df['Date of Admission']


# In[32]:


df.head()


# In[33]:


df.to_csv(r"C:\Users\Antonio\Desktop\Temp\health.csv", index=False)


# In[ ]:





# In[ ]:





# In[ ]:




