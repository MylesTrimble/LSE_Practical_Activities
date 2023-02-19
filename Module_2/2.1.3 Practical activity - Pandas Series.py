#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# **Emergency Numbers**

# In[3]:


# Create a dictionary
dict_1 = {'123': 'Law Endorcement',
          '224': 'Fire and Rescue Service',
          '101': 'Emergency Meducal Service',
          '999': 'Emergency Management',
          '900': 'Public Works'}

# Create a Series 
emergency_numbers = pd.Series(dict_1)

# View the result by passing or calling the print() function
print(emergency_numbers)


# **Emergency Protocols**

# In[7]:


# Create a list
list_1 = ['Prevention', 'mitigation', 'preparedness', 'response', 'recovery']

# Create a Series
emergency_protocols = pd.Series(list_1)

print(emergency_protocols)


# OR

# In[9]:


# Create a numbered list
emergency_protocols = pd.Series(['Prevention', 'Mitigation',
                                 'Preparedness', 'Response', 
                                 'Recovery'],
                                index = ['1', '2', '3', '4', '5'])

# View the DataFrame
print(emergency_protocols)


# **Emergency Checklist**

# In[8]:


# Create a Series from a list
checklist = ['Check carotid pulse (neck)', 'Check breathing (nose)',
             'Check for obstructions (nose, ears, mouth)', 
             'Check pupils (responsive)', 'Consciousness',
             'Contact details', 'Any allergies']

emergency_checklist = pd.Series(checklist)

# View the DataFrame
print(emergency_checklist)

