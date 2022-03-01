#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')


# In[4]:


df.head()


# In[5]:


df.shape


# In[76]:


dates=df.columns[4:][2]
dates


# In[11]:


for date in dates: 
    print(date)


# # Total Copnfom Cases

# In[19]:


total_cases=[]
for date in dates: 
#      print(df[date].sum())
    total_cases.append(df[date].sum())

print(total_cases)


# In[24]:


plt.figure(figsize=(10,6))
sns.lineplot(x=days_since,y=total_cases,color='r',marker='*')


# In[25]:


df.columns


# In[33]:


# days_since = [i for i in range(len(dates))]
# days_since
# len(dates)

days_num=[i for i in range(len(dates))]
days_num


# In[38]:


plt.figure(figsize=(10,8))
sns.lineplot(
    x=days_num,
    y=total_cases,color='r',marker='*'
)
plt.title('World Total confirmed cases- {:.2f} million'.format(total_cases[-1]/10**6),fontweight='bold',size=20)
plt.xlabel('No of days since 22 Jan 2020',size=15)
plt.ylabel('World Covid Count',size=15)
plt.show()


# In[39]:


def per_day_rise(x):
    per_day_rise = []

    for i in range(len(x)):
        if i==0:
            per_day_rise.append(0)
        else:
            per_day_rise.append(x[i]-x[i-1])

    return per_day_rise


# In[40]:


plt.figure(figsize = (10,6))
sns.lineplot(x=days_since,y=per_day_rise(total_cases),color='r',marker='*')
plt.title('World per day rise in confirmed cases',fontweight='bold',size=20)
plt.xlabel('No of days since 22 Jan 2020',size=15)
plt.ylabel('World per day rise',size=15)
plt.show()


# In[42]:


top_5_con = df.iloc[:,[1,-1]].sort_values(by=dates[-1],ascending =False)[:5]
top_5_con


# In[50]:


df.iloc[[2]]


# In[70]:


df.iloc[:,[1,-1]].sort_values(by=dates[1],ascending =False)[:5]


# In[79]:


# df.iloc[:,[1,-1]].sort_values(by=)
dates[-1]


# In[84]:


dates=df.columns[4:]
dates


# In[85]:


dates[-1]


# In[97]:


top_5_con=df.iloc[:,[1,-1]].sort_values(by=dates[-1],ascending =False)[:5]
top_5_con.columns=['Country/Region','Total Confirmed']
top_5_con=top_5_con.reset_index(drop=True)
top_5_con


# In[99]:


plt.figure(figsize=(10,6))
sns.barplot(x='Country/Region',y='Total Confirmed',data=top_5_con)


# In[ ]:




