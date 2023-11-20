#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Checking working directory
import os
import pandas as pd

current_directory = os.getcwd()
print(current_directory)


# In[2]:


# Change working directory
new_directory_path = r'/Users/jennajohnson'
os.chdir(new_directory_path)


# In[3]:


updated_dir = os.getcwd()
print(updated_dir)


# In[4]:


try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except filenotFoundError:
        print(f"file '{file_path}' not found.")
except IOError:
        print("An error occurred while reading this file.")


# In[5]:


# Average Number of Patients
df = pd.read_csv(file_path)


# In[6]:


print(df)


# In[7]:


print(df.columns)


# In[8]:


# Average Age
average_age = df[' Age'].mean()
print(average_age)


# In[9]:


# Get the highest blood pressure
max_bp = max(df[' BloodPressure'])
print(f"The highest blood pressure is {max_bp}.")


# In[10]:


# Get the lowest blood pressure
low_bp = min(df[' BloodPressure'])
print(f"The lowest blood pressure is {low_bp}.")


# In[ ]:


# Average temperature
average_temp = df[' Temperature'].mean()
print(f"The average temperature is {average_temp}")

