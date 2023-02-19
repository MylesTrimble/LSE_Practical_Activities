#!/usr/bin/env python
# coding: utf-8

# In[5]:


# 1

from datetime import time
t = time(14, 42, 5, 566)

print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("microsecond:", t.microsecond)


# In[8]:


# 2

from datetime import datetime
dt = datetime(2019, 2, 28, 23, 55, 59, 1023)

print("Year:", dt.year)
print("Month:", dt.month)
print("Day:", dt.day)
print("hour:", dt.hour)
print("minute:", dt.minute)
print("Second:", dt.second)
print("microsecond:", dt.microsecond)


# In[12]:


# 3

from datetime import date
today = date.today()

print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)


# In[20]:


# 4

from datetime import datetime

day = datetime(2017, 1, 28)

print("Origninal data:", day)
print("Day name:", day.strftime('%A'))

