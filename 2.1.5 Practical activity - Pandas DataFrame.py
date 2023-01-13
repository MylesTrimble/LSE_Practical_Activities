#!/usr/bin/env python
# coding: utf-8

# # Leave Configuration

# In[1]:


# Import pandas library
import pandas as pd


# In[8]:


# Create a DataFrame from a dictionary
data = {'Name': ['Shen Lee', 'Leon Buhle', 'Tracy Adams',
                 'Lebo Sinuka', 'Lauren Pierce', 'Monika Bond',
                 'Natahs Allsopp', 'Nicholas Winter',
                 'Christopher Eckson', 'Siobhan OMalley'],
        'Annual': [23, 20, 15, 19, 21, 21, 10, 15, 16, 23],
        'Sick': [10, 8, 10, 9, 7, 10, 9, 10, 8, 5],
        'Personal': [5, 4, 5, 0, 5, 2, 5, 4, 2, 5],
        'Bonus': [3, 0, 0, 3, 3, 6, 0, 3, 6, 3]}
row_labels = [215, 216, 217, 218, 219, 220, 221, 222, 223, 224]
leave_cycle = pd.DataFrame(data, columns=['Name', 'Annual',
                                          'Sick', 'Personal', 'Bonus'],
index = row_labels)

leave_cycle.index.name = 'Personnel_ID'

# View the DataFrame
leave_cycle


# **Added Columns**

# In[10]:


# Create a DataFrame from a dictionary
data = {'Name': ['Shen Lee', 'Leon Buhle', 'Tracy Adams',
                 'Lebo Sinuka', 'Lauren Pierce', 'Monika Bond',
                 'Natahs Allsopp', 'Nicholas Winter',
                 'Christopher Eckson', 'Siobhan OMalley'],
        'Annual': [23, 20, 15, 19, 21, 21, 10, 15, 16, 23],
        'Sick': [10, 8, 10, 9, 7, 10, 9, 10, 8, 5],
        'Personal': [5, 4, 5, 0, 5, 2, 5, 4, 2, 5],
        'Bonus': [3, 0, 0, 3, 3, 6, 0, 3, 6, 3],
        'Total leave taken': [0, 3, 5, 10, 5, 8, 11, 9, 15, 5],
        'Total leave available': [38, 32, 30, 28, 33, 33, 24, 29, 26, 33],
        'Annual total': [38, 35, 35, 38, 38, 41, 35, 38, 41, 38],
        'Total leave left to take': [38, 29, 25, 18, 28, 25, 13, 20, 11, 28]}
row_labels = [215, 216, 217, 218, 219, 220, 221, 222, 223, 224]
leave_cycle = pd.DataFrame(data, columns=['Name', 'Annual',
                                          'Sick', 'Personal', 'Bonus',
                                          'Total leave taken',
                                          'Total leave available',
                                          'Total leave left to take'],
index = row_labels)
leave_cycle.index.name = 'Personnel_ID'

# View the DataFrame
leave_cycle


# In[ ]:




