import pandas as pd

# import data
df1 = pd.read_csv('/Users/camille/Documents/CA675 Cloud Technologies/Assignment1/Data/top1.csv')
df2 = pd.read_csv('/Users/camille/Documents/CA675 Cloud Technologies/Assignment1/Data/top2.csv')
df3 = pd.read_csv('/Users/camille/Documents/CA675 Cloud Technologies/Assignment1/Data/top3.csv')
df4 = pd.read_csv('/Users/camille/Documents/CA675 Cloud Technologies/Assignment1/Data/top4.csv')

# combine four CSV files
post = df1.append(df2)
post = post.append(df3)
post = post.append(df4)

# show data information
post.info()


# In[3]:


# check how many unique post data there are
post.Id.nunique()


# In[4]:


# check the index of each row
post.index


# In[5]:


# so I need to reset the post's index to 0~199999
post.index.nunique()


# In[6]:


# reset post's index
post.reset_index(drop=True, inplace=True)
post.index


# In[7]:


post.index.nunique()


# In[9]:


# check the first five data
post.head()


# Because some elements of Body colunms includes '\r', '\n' and '\t',and will cause some problem when load the csv file into pig, so I need to clean them.

# In[10]:


# check if '\r' exist and count how many items includes '\r'
(post['Body'].str.contains("\r")==True).value_counts()


# In[11]:


# check if '\n' exist and count how many items includes '\n'
(post['Body'].str.contains("\n")==True).value_counts()


# In[12]:


# check if '\t' exist and count how many items includes '\t'
(post['Body'].str.contains("\t")==True).value_counts()


# In[13]:


(post['Body'].str.contains("\v")==True).value_counts()


# In[14]:


post.Body[1713]


# In[15]:


# delete them
post['Body'] = post['Body'].apply(lambda x:x.replace('\n', ''))
post['Body'] = post['Body'].apply(lambda x:x.replace('\r', ''))
post['Body'] = post['Body'].apply(lambda x:x.replace('\t', ''))
post['Body'] = post['Body'].apply(lambda x:x.replace('\v', ''))
post['Body'] = post['Body'].apply(lambda x:x.replace('\f', ''))


# In[42]:


(post['Body'].str.contains("\n")==True).value_counts()


# In[17]:


# check if this operation works
(post['Body'].str.contains("\r")==True).value_counts()


# In[18]:


(post['Body'].str.contains("\t")==True).value_counts()


# In[19]:


(post['Body'].str.contains("\v")==True).value_counts()


# In[20]:


(post['Body'].str.contains("\f")==True).value_counts()


# In[21]:


post.Body[1713]


# In[23]:


(post['Title'].str.contains("\t")==True).value_counts()


# In[24]:


post['Title'] = post['Title'].apply(lambda x:x.replace('\t', ''))


# In[25]:


(post['Title'].str.contains("\t")==True).value_counts()


# In[27]:


# delete them
post['Title'] = post['Title'].apply(lambda x:x.replace('\n', ''))
post['Title'] = post['Title'].apply(lambda x:x.replace('\r', ''))
post['Title'] = post['Title'].apply(lambda x:x.replace('\t', ''))
post['Title'] = post['Title'].apply(lambda x:x.replace('\v', ''))
post['Title'] = post['Title'].apply(lambda x:x.replace('\f', ''))


# In[29]:


(post['Body'].str.contains(",")==True).value_counts()


# In[30]:


post['Body'] = post['Body'].apply(lambda x:x.replace(',', ''))


# In[40]:


(post['Body'].str.contains(",")==True).value_counts()


# In[32]:


(post['Title'].str.contains(",")==True).value_counts()


# In[33]:


post['Title'] = post['Title'].apply(lambda x:x.replace(',', ''))


# In[41]:


(post['Title'].str.contains(",")==True).value_counts()


# In[36]:


post.to_csv('/Users/camille/Documents/CA675 Cloud Technologies/Assignment1/cleaningdata.csv')
