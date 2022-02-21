#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


dataset = pd.read_csv("Social_Network_Ads.csv")


# In[4]:


dataset.head()


# In[5]:


dataset.columns


# In[6]:


dataset[['Age']]


# In[7]:


X = dataset[['Age', 'EstimatedSalary' ] ] 


# In[8]:


y = dataset['Purchased']


# In[9]:


type(X)


# In[10]:


X = X.values


# In[11]:


type(X)


# In[12]:


y = y.values


# In[13]:


type(y)


# In[14]:


from sklearn.model_selection import train_test_split


# In[15]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)


# In[16]:


from sklearn.neighbors import KNeighborsClassifier


# In[17]:


model = KNeighborsClassifier(n_neighbors=3)


# In[18]:


model.fit(X_train, y_train)


# In[19]:


y_pred = model.predict(X_test)


# In[20]:


y_pred


# In[21]:


y_test


# In[22]:


from sklearn.metrics import confusion_matrix


# In[23]:


confusion_matrix(y_test, y_pred)


# In[24]:


from sklearn.metrics import accuracy_score


# In[25]:


print(accuracy_score(y_test, y_pred))


# In[ ]:




