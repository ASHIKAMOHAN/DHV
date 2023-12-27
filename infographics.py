import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Original data URI
Original_dataUri = 'Life-Expectancy-Data-Updated.csv'

# List of countries to filter
countryList = ["Belgium", "India", "United Arab Emirates", "Bangladesh", "Brazil", "Canada", "South Africa", "Kuwait"]

# Load the data
data = pd.read_csv(Original_dataUri)

# Filter data by countries in countryList
filtered_data = data[data["Country"].isin(countryList)]
# Get rid of any empty data
filtered_data.dropna(inplace=True)
# Save filtered data to CSV
filtered_data.to_csv("filtered.csv", index=False)

# Visualize life expectancy over the years
plt.figure(figsize=(10, 6))
sns.lineplot(x='Year', y='Life_expectancy', data=filtered_data, hue='Region')
plt.title('Life Expectancy Over the Years by Region')
plt.xlabel('Year')
plt.ylabel('Life Expectancy')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()

# Distribution of infant deaths
plt.figure(figsize=(8, 6))
sns.histplot(filtered_data['Infant_deaths'], bins=20, kde=True)
plt.title('Distribution of Infant Deaths')
plt.xlabel('Infant Deaths per 1000 Population')
plt.ylabel('Frequency')
plt.show()
