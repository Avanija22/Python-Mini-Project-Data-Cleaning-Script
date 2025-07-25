# -*- coding: utf-8 -*-
"""DataCleaning.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14GfspcaBI7PeodzvNLK4eNUq8r7zg2Zv
"""

!pip install pandas matplotlib

import pandas as pd
import matplotlib.pyplot as plt

file_path = 'dirty_data_for_cleaning.csv'
df = pd.read_csv(file_path)

df_cleaned = df.drop_duplicates()

df_cleaned['Name'] = df_cleaned['Name'].fillna('Unknown')
df_cleaned['Email'] = df_cleaned['Email'].fillna('missing@email.com')
df_cleaned['PhoneNumber'] = df_cleaned['PhoneNumber'].fillna('Unavailable')
df_cleaned['Age'] = df_cleaned['Age'].fillna(df_cleaned['Age'].mean().round(0))
df_cleaned['Country'] = df_cleaned['Country'].fillna('Unknown')
df_cleaned['Salary'] = df_cleaned['Salary'].fillna(df_cleaned['Salary'].mean().round(0))
df_cleaned['JoiningDate'] = df_cleaned['JoiningDate'].fillna('2025-01-04')

df_cleaned['JoiningDate'] = pd.to_datetime(df_cleaned['JoiningDate'])

#Data Visualization

country_count = df_cleaned['Country'].value_counts()
plt.figure(figsize=(8,5))
country_count.plot(kind ='bar')
plt.title('Count of Employees by Country')
plt.xlabel('Country')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8,5))
df_cleaned['Age'].hist(bins=10, edgecolor='black')
plt.title('Age Distribution of Employees')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(8,5))
df_cleaned['Salary'].hist(bins=10, edgecolor='black', color = 'green')
plt.title('Salary Distribution of Enployees')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()

cleaned_file_path = "clean_data.csv"
df_cleaned.to_csv(cleaned_file_path, index=False)
