import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd

# Original data URI
Original_dataUri = 'owid-covid-data (1).csv'

column_names = ["location", "date", "total_cases_per_million", "total_deaths_per_million", "reproduction_rate",
                 "population_density", "gdp_per_capita", "life_expectancy", "human_development_index",
                 "total_vaccinations_per_hundred"]

# List of countries to filter
countryList = ["Africa", "Brazil", "Canada", "China", "Germany", "India", "Italy", "Malaysia", "Nepal", "Portugal",
               "Sri Lanka", "United Arab Emirates", "United Kingdom", "United States"]

# Load the data
data = pd.read_csv(Original_dataUri)

# Filter data by countries in countryList
filtered_data = data[data["location"].isin(countryList)]

# Delete columns with more than 75% null values
filtered_data = filtered_data.dropna(thresh=0.75 * len(filtered_data), axis=1)
filtered_data = filtered_data.fillna(0)

# Filter columns
filtered_columns = [col for col in filtered_data.columns if col in column_names]
filtered_df = filtered_data[filtered_columns]
filtered_data.to_csv("filtered.csv")

# Filter data for the year 2023
data_2023 = filtered_df[filtered_df["date"].str.startswith("2023")]

# Plot bar graph
plt.figure(figsize=(12, 6))
plt.bar(data_2023["location"], data_2023["total_deaths_per_million"])
plt.xlabel('Countries')
plt.ylabel('Total deaths per Million (2023)')
plt.title('Total deaths per Million in 2023 by Country')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

