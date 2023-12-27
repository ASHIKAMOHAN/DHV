import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Original data URI
Original_dataUri = 'Life Expectancy Data.csv'

# List of countries to filter
countryList = [ "Belgium","India", "United Arab Emirates","Bangladesh",
               "Brazil","Canada","South Africa","Kuwait"]

# Load the data
data = pd.read_csv(Original_dataUri)

# Filter data by countries in countryList
filtered_data = data[data["Country"].isin(countryList)]

# Delete columns with more than 75% null values
filtered_data = filtered_data.dropna(thresh=0.75 * len(filtered_data), axis=1)
filtered_data = filtered_data.fillna(0)
# filtered_data.to_csv("filtered.csv")

# Filter data for the year 2015
filtered_data_2015 = filtered_data[filtered_data['Year'] == 2015]

# Create a bar chart for Adult Mortality in 2015
plt.figure(figsize=(12, 6))
plt.bar(filtered_data_2015["Country"], filtered_data_2015["Adult Mortality"], color='blue')
plt.xlabel('Country')
plt.ylabel('Adult Mortality')
plt.title('Adult Mortality in 2015 for Selected Countries')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
for country in countryList:
    country_data = filtered_data[filtered_data["Country"] == country]
    plt.plot(country_data["Year"], country_data["Life expectancy "], label=country, marker='o')

plt.xlabel('Year')
plt.ylabel('Life Expectancy')
plt.title('Life Expectancy Over Time for Selected Countries')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


status_counts = filtered_data['Status'].value_counts()

# Display the counts
print(status_counts)
plt.boxplot([filtered_data[filtered_data['Status']=='Developing']['Life expectancy '], filtered_data[filtered_data['Status']=='Developed']['Life expectancy ']], labels=['Developing','Developed'])
plt.ylabel('Life expectancy')
plt.xlabel('Countries')
plt.show()

sns.lineplot(x=filtered_data['GDP'], y=filtered_data['Life expectancy '])
plt.xlabel('GDP')
plt.ylabel('Life Expectancy')
plt.title('Relationship between GDP and Life Expectancy')
plt.show()

sorted_data = filtered_data.sort_values(by="percentage expenditure", ascending=False)

plt.figure(figsize=(12, 6))
plt.barh(sorted_data["Country"], sorted_data["percentage expenditure"], color='red')
plt.xlabel('Percentage Expenditure')
plt.ylabel('Country')
plt.title('Percentage Expenditure for Selected Countries')
plt.tight_layout()
plt.show() 



