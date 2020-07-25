#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


Russia = pd.read_csv("Downloads/crime.csv")
type(Russia)


# In[3]:


Russia #dataset


# In[4]:


len(Russia) #number of rows


# In[5]:


Russia.shape #(rows, columns)


# In[6]:


Russia.head() #First couple of rows


# In[7]:


Russia.tail() #last couple of rows


# In[8]:


Russia.tail(3) #last three rows


# In[9]:


Russia.tail(5) #Last five rows


# In[10]:


Russia.head(5) #First five rows


# In[11]:


Russia.head(3) #First three rows


# In[12]:


Russia.info() #columns and their datatypes


# In[13]:


Russia.describe() #Information on the columns of the dataset


# In[14]:


import numpy as np
Russia.describe(include=np.object)


# In[15]:


Russia["Fraud_scam"].value_counts()


# In[16]:


Russia


# In[17]:


pd.set_option("display.max.rows", None) #Displaying the maximum number of rows


# In[18]:


Russia #Dataset with the maximum number of rows


# In[59]:


Russia2019 = Russia.tail(11) #last eleven rows


# In[20]:


Russia.keys() #names of the columns in the array


# In[21]:


Russia["Total_crimes"].max() #maximum number of total crimes


# In[22]:


Russia["month"].max() #maximum month


# In[23]:


Russia["Terrorism"].agg(("min", "max")) #Minimum and maximum of the number of terroristic crimes


# In[24]:


Russia["Total_crimes"].sum() #Sum of the total number of crimes throughout the entire dataset


# In[25]:


Russia["Terrorism"].sum() #Sum of the total number of terroristic crimes


# In[26]:


Russia["Weapons"].agg(("min", "max")) #minimum and maximum number of the total number of crimes of weapons throughout the entire dataset


# In[27]:


"totalcrimes" in Russia.keys() #Checking if there is a column called totalcrimes


# In[28]:


"Total_crimes" in Russia.keys() #Checking if there is a colum called Total_crimes


# In[29]:


Russia.iloc[-2] #Second to last row


# In[30]:


Russia.iloc[-3] #Third to last row


# In[31]:


Russia5 = Russia.head(12) #First nine rows dealing with 2003
Russia5


# In[32]:


len(Russia5)


# In[33]:


Russia5.shape #rows, columns


# In[34]:


Russia5.info()


# In[35]:


Russia5.describe()


# In[36]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plot1 = Russia5.plot(x = "month", y = "Total_crimes") #Graph of the total crimes throughout the months in 2003
x = plt.xlabel('month')
y = plt.ylabel('total crime')
plot1.set_xticklabels(plot1.get_xticklabels(), rotation=45)


# In[37]:


Russia6 = Russia.tail(13)
plot2 = Russia6.plot(x = "month", y = "Total_crimes") #Graph of the total crimes throughout the months in 2019 and one in month in 2020
x = plt.xlabel('month')
y = plt.ylabel('total crime')
plot2.set_xticklabels(plot2.get_xticklabels(), rotation=45)    


# In[38]:


datacombined = pd.concat([Russia5, Russia6], sort=False) #Dataset from 2003 and dataset from 2019 and a little bit of 2020 combined
datacombined


# In[39]:


plot3 = datacombined.plot(x = "month", y = "Total_crimes") #Graph of the total crimes throughout the months in 2003 and in 2019 and some of 2020
x = plt.xlabel('month')
y = plt.ylabel('total crime')
plt.title('total crime vs month')
plot3.set_xticklabels(plot3.get_xticklabels(), rotation=45) 


# In[40]:


import matplotlib.pyplot as plt
histogram = plt.hist(Russia["Total_crimes"], bins = 5)
x = plt.xlabel('number of total crimes')
y = plt.ylabel('frequency')
plt.show()


# In[41]:


import matplotlib.pyplot as plt
histogram = plt.hist(Russia["Terrorism"], bins = 7)
x = plt.xlabel('number of terroristic crimes')
y = plt.ylabel('frequency')
plt.show()


# In[42]:


import seaborn as sns
sns.distplot(Russia['Total_crimes'], bins=9)
x = plt.xlabel('number of total crimes')
y = plt.ylabel('frequency')
plt.title('frequency vs number of total crimes')
plt.xlim(150000, 350000)
plt.show()


# In[43]:


sns.distplot(Russia['Terrorism'], bins=7)
x = plt.xlabel('number of terroristic crimes')
y = plt.ylabel('frequency')
plt.title('frequency vs number of terroristic crimes')
plt.show()


# In[44]:


filtering = Russia[Russia["Total_crimes"] < 200000]
filtering


# In[45]:


plot4 = filtering.plot(x = "month", y = "Total_crimes") #Graph of the total crimes throughout the months in 2003 and in 2019 and some of 2020
x = plt.xlabel('month')
y = plt.ylabel('total crime')
plt.title('total crime vs month')
plot4.set_xticklabels(plot4.get_xticklabels(), rotation=45) 


# In[46]:


sns.distplot(filtering['Terrorism'], bins=7)
x = plt.xlabel('number of terroristic crimes')
y = plt.ylabel('frequency')
plt.title('frequency vs number of terroristic crimes')
plt.xlim(0,300)
plt.show()


# In[47]:


filtering.describe()


# In[48]:


Russia7 = Russia.loc[0:204, ["month", "Total_crimes"]]
Russia7


# In[49]:


Russia7["Total_crimes"].agg(("min", "max"))


# In[51]:


crime = Russia7["Total_crimes"]
crime.sum()


# In[58]:


month = Russia5["month"]
Totalcrimes = Russia5["Total_crimes"]
plt.scatter(month, Totalcrimes, edgecolors='r')
plt.xlabel('Month')
plt.ylabel('Total crimes')
plt.title('Total crimes vs Month')
plt.xticks(rotation = 80)
plt.show()


# In[61]:


month = Russia2019["month"]
Totalcrimes = Russia2019["Total_crimes"]
plt.scatter(month, Totalcrimes, edgecolors='r')
plt.xlabel('Month')
plt.ylabel('Total crimes')
plt.title('Total crimes vs Month')
plt.xticks(rotation = 80)
plt.show()


# In[ ]:




