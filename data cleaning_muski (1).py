#!/usr/bin/env python
# coding: utf-8

# # 1.IMPORTING THE LIBRARIES AND LOADING THE DATASET 

# In[1]:


import pandas as pd
df = pd.read_csv(open('laptopData.csv'))


# # 2.INSPECTING THE DATA
# 

# In[2]:


df.info()


# In[3]:


df.describe()


# In[4]:


df.describe(include=['object'])


# In[5]:


df.head()


# # 3.FINDING THE MIXED DATATYPES
# 

# In[6]:


# Function to clean and convert columns to the appropriate types
def clean_data(df):
    # Convert 'Inches' to numeric (ignore errors)
    df['Inches'] = pd.to_numeric(df['Inches'], errors='coerce')

    # Clean and convert 'Ram' (convert to string, remove 'GB', then convert to float)
    df['Ram'] = df['Ram'].astype(str).str.replace('GB', '', regex=False).astype(float)

    # Clean and convert 'Weight' (convert to string, handle '?', remove 'kg', then convert to float)
    df['Weight'] = df['Weight'].astype(str).replace('?', None)
    df['Weight'] = df['Weight'].str.replace('kg', '', regex=False).astype(float)

    # Apply memory conversion logic after ensuring values are treated as strings
    df['Memory'] = df['Memory'].apply(lambda x: convert_memory(str(x)))

    return df


# In[7]:


# Function to handle 'Memory' conversions
def convert_memory(memory_string):
    if 'GB' in memory_string:
        return float(memory_string.replace('GB', '').split()[0])
    elif 'TB' in memory_string:
        return float(memory_string.replace('TB', '').split()[0]) * 1024  # Convert TB to GB
    else:
        return None  # If format is unexpected, return None


# In[8]:


# Clean the dataset
cleaned_data = clean_data(df)


# In[9]:


# Check if the cleaning worked
cleaned_data.info()
cleaned_data.head()


# # 4.REPLACING STRING

# In[10]:


import pandas as pd

# Sample DataFrame
data = {'Ram': ['8GB', '16GB', '32GB', '?'], 'Weight': ['1.5kg', '2.2kg', '?', '3.0kg']}
df = pd.DataFrame(data)

# Replace '?' with None (missing values)
df['Ram'] = df['Ram'].replace('?', None)
df['Weight'] = df['Weight'].replace('?', None)

# Remove 'GB' from 'Ram' column and convert to numeric
df['Ram'] = df['Ram'].astype(str).str.replace('GB', '').astype(float)

# Remove 'kg' from 'Weight' column and convert to numeric
df['Weight'] = df['Weight'].astype(str).str.replace('kg', '').astype(float)

# Display cleaned DataFrame
print(df)


# # 5.REMOVING ROWS

# In[11]:


# Remove rows where any column has a missing value
df_cleaned = df.dropna()


# In[12]:


# Remove rows where 'Ram' is less than or equal to 0 or missing
df_cleaned = df[df['Ram'] > 0]


# In[13]:


# Sample DataFrame
data = {'Ram': ['8GB', '16GB', '?', '32GB'], 'Weight': ['1.5kg', '2.2kg', '3.0kg', '?']}
df = pd.DataFrame(data)

# Remove rows where 'Ram' or 'Weight' contain '?'
df_cleaned = df[(df['Ram'] != '?') & (df['Weight'] != '?')]

# Display cleaned DataFrame
print(df_cleaned)


# # 6.DUPLICATES

# In[14]:


import pandas as pd

# Sample DataFrame with duplicates
data = {'Ram': ['8GB', '16GB', '8GB', '32GB'],
        'Weight': ['1.5kg', '2.2kg', '1.5kg', '3.0kg']}
df = pd.DataFrame(data)

# 1. Find duplicate rows
duplicates = df[df.duplicated()]
print("Duplicate rows:")
print(duplicates)

# 2. Remove duplicate rows, keeping only the first occurrence
df_cleaned = df.drop_duplicates()
print("\nDataFrame after removing duplicates:")
print(df_cleaned)


# In[15]:


# Remove duplicates based only on the 'Ram' column
df_cleaned = df.drop_duplicates(subset=['Ram'], keep='first')


# # 7.SORTING DATA

# In[16]:


# Sample DataFrame
data = {'Ram': ['8GB', '16GB', '32GB', '4GB'],
        'Weight': ['2.0kg', '1.5kg', '2.5kg', '2.3kg']}
df = pd.DataFrame(data)

# Sorting by 'Ram' in ascending order
df_sorted = df.sort_values(by='Ram', ascending=True)

print("Sorted DataFrame by 'Ram':")
print(df_sorted)


# # 8.MISSING DATA

# In[21]:


# Check for null values in the dataset
null_values = df.isnull().sum()
print(null_values)


# In[22]:


# Remove rows with null values
cleaned_df = df.dropna()
print(cleaned_df)


# In[23]:


# Display the null value count before cleaning and the cleaned data
null_values, cleaned_df.head()


# In[ ]:




