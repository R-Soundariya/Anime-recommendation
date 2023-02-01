#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from scipy.spatial import distance


# In[3]:


data=pd.read_csv('anime.csv')


# In[4]:


data.head()


# In[5]:


genre=data['genre'].values


# In[6]:


data.info()


# In[7]:


lis=[]
for i in genre:
    i=str(i)
    for p in i.split(','):
        if p not in lis:
            lis.append(p)


# In[8]:


len(lis)


# In[9]:


dic={}


# In[10]:


t=[]
for i in genre:
    for j in lis:
        dic[j]=0
    i=str(i)
    for p in i.split(','):
        dic[p]+=1
    t.append(list(dic.values()))      


# In[11]:


len(t[0])


# In[12]:


X=np.array(t)


# In[13]:


s=input('Enter the anime you like and we will find more like those for you  :')
num=int(input('Please enter the number of recommendations you want:'))
name=data['name'].values
for i in range(len(name)):
    name[i]=name[i].lower()
s=s.lower()
h=-1
for i in range(len(name)):
    if s in name[i]:
        h=i
        break
imp=[]
if h==-1:
    print('Sorry No match found :(')
else:
    for i in range(len(t)):
        if i==h:
            continue
        else:
            if len(imp)<num:
                imp.append([distance.euclidean(t[i], t[h]),t[i],i])
            else:
                imp.sort()
                if imp[num-1][0]>distance.euclidean(t[i],t[h]):
                    del imp[num-1]
                    imp.append([distance.euclidean(t[i],t[h]),t[i],i])
    name=data['name'].values
    print('The anime recommended for you are :')
    count=0
    for i in imp:
        count+=1
        print(count,'. ',name[i[2]])

