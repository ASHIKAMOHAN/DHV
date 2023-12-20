import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Original data URI
Original_dataUri = 'owid-covid-data 2.csv'

column_names=["location","date","total_cases_per_million", "total_deaths_per_million", "reproduction_rate",
                   "population_density", "gdp_per_capita", "life_expectancy", "human_development_index",
                   "total_vaccinations_per_hundred"]

# List of countries to filter
countryList = ["Africa", "Brazil", "Canada", "China", "Germany", "India", "Italy", "Malaysia", "Nepal", "Portugal",
               "Sri Lanka", "United Arab Emirates", "United Kingdom", "United States"]

# Load the data
data = pd.read_csv(Original_dataUri)

# Filter data by countries
filtered_data = data[data["location"].isin(countryList)]

# Delete columns with more than 75% null values
filtered_data = filtered_data.dropna(thresh=0.75 * len(filtered_data), axis=1)
filtered_data = filtered_data.fillna(0)

filtered_data.to_csv("filtred.csv")
# Fill remaining empty columns with mean (exclude non-numeric columns)
numeric_columns = filtered_data.select_dtypes(include=np.number).columns
filtered_data[numeric_columns] = filtered_data[numeric_columns].apply(lambda col: col.fillna(col.mean()) if col.isnull().any() else col, axis=0)

# Print the resulting DataFrame
print(filtered_data.head())
# Save the resulting DataFrame to a new CSV file
# filtered_data.to_csv('filtered_data.csv', index=False)

filtered_columns=[col for col in data.columns if col in column_names]
filtered_df=data[filtered_columns]
cleaned_df = filtered_df.fillna(0)
# cleaned_df.to_csv("filtred.csv")

# Convert the 'date' column to datetime format
filtered_data['date'] = pd.to_datetime(filtered_data['date'])

# Filter data for the year 2022
data_2022 = filtered_data[filtered_data['date'].dt.year == 2022]

# Aggregate data by country
agg_data = data_2022.groupby('location')['total_cases_per_million'].sum().reset_index()

# Plot a bar graph
plt.figure(figsize=(12, 6))
plt.bar(agg_data['location'], agg_data['total_cases_per_million'])
plt.xlabel('Countries')
plt.ylabel('Total Cases per Million')
plt.title('Total Cases per Million in 2022 by Country')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
plt.tight_layout()
plt.show()
