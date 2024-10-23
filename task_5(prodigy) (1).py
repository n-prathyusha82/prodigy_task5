# -*- coding: utf-8 -*-
"""Task_5(Prodigy)

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IaYiwX_Kcou2txP5m9k_2D0byR3hZbI1

**Import the necessary libraries**
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""**Load the Dataset**"""

from google.colab import files
uploaded = files.upload()

"""**After uploading, load the dataset:**"""

df = pd.read_csv('accident_data.csv')

"""**Data Exploration and Cleaning**"""

df.head()

"""**Identify and handle missing values:**"""

df.isnull().sum()

"""**Drop or fill any missing values in important columns like weather, road conditions, and time of day:**"""

df.dropna(subset=['Weather_Condition', 'Road_Condition', 'Start_Time'], inplace=True)

"""**Convert the Start_Time column to datetime format and extract Time of Day information:**"""

df['Start_Time'] = pd.to_datetime(df['Start_Time'])
df['Hour'] = df['Start_Time'].dt.hour

"""**Create a column for Time of Day:**"""

def get_time_of_day(hour):
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 22:
        return 'Evening'
    else:
        return 'Night'

df['Time_of_Day'] = df['Hour'].apply(get_time_of_day)

"""**Accidents by Time of Day and Road Conditions:**"""

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Time_of_Day', hue='Road_Condition')
plt.title('Accidents by Time of Day and Road Conditions')
plt.show()

"""**Accidents by Time of Day and Weather Conditions:**"""

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Time_of_Day', hue='Weather_Condition')
plt.title('Accidents by Time of Day and Weather Conditions')
plt.xticks(rotation=45)
plt.show()

"""**Create a scatter plot of accidents by location**"""

plt.figure(figsize=(10, 8))
sns.scatterplot(data=df, x='Start_Lng', y='Start_Lat', hue='Time_of_Day', alpha=0.6)
plt.title('Accident Hotspots')
plt.show()

"""**To save the cleaned dataset:**"""

df.to_csv('cleaned_accident_data.csv', index=False)
from google.colab import files
files.download('cleaned_accident_data.csv')

plt.savefig('plot_name.png')
files.download('plot_name.png')