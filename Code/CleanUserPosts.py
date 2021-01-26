#!/usr/bin/env python
# coding: utf-8

# In[331]:


import pandas as pd
import re
import os
os.getcwd()
df = pd.read_csv('/Users/camille/Documents/CA675 Cloud Technologies/Assignment1/top_10_posts.csv', header=None)


# In[332]:


df


# In[333]:


df[1] = df[1] + df[2]


# In[334]:


# Use regular expression to clean Body and Title
df[1] = df[1].apply(lambda x: re.sub('<.*?>',' ', x))
df[2] = df[2].apply(lambda y: re.sub('<.*?>',' ', y))

df[1] = df[1].apply(lambda x: re.sub('\\n*\\t*\\r*\\s+',' ', x))
df[2] = df[2].apply(lambda y: re.sub('\\n*\\t*\\r*\\s+',' ', y))


# In[335]:



df[1] = df[1].apply(lambda x:x.replace('{', ' '))
df[1] = df[1].apply(lambda x:x.replace('}', ' '))
df[1] = df[1].apply(lambda x:x.replace('(', ' '))
df[1] = df[1].apply(lambda x:x.replace(')', ' '))
df[1] = df[1].apply(lambda x:x.replace('[', ' '))
df[1] = df[1].apply(lambda x:x.replace(']', ' '))
df[1] = df[1].apply(lambda x:x.replace('<', ' '))
df[1] = df[1].apply(lambda x:x.replace('>', ' '))
df[1] = df[1].apply(lambda x:x.replace('+', ' '))
df[1] = df[1].apply(lambda x:x.replace('/', ' '))
df[1] = df[1].apply(lambda x:x.replace('*', ' '))
df[1] = df[1].apply(lambda x:x.replace(';', ' '))
df[1] = df[1].apply(lambda x:x.replace('=', ' '))
df[1] = df[1].apply(lambda x:x.replace(':', ' '))
df[1] = df[1].apply(lambda x:x.replace("'", ' '))
df[1] = df[1].apply(lambda x:x.replace('"', ' '))


# In[336]:


df[1] = df[1] + df[3]

df[1] = df[1].apply(lambda x:x.replace('<', ' '))
df[1] = df[1].apply(lambda x:x.replace('>', ' '))


# In[337]:


df = df.drop([2,3],axis=1)


# In[338]:


df


# In[339]:


df[1][0]


# In[340]:


df[1][421]


# In[341]:


df.to_csv('cleaned_posts.txt',index = False, header = False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




