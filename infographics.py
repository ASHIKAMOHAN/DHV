import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Original data URI
Original_dataUri = 'owid-covid-data 2.csv'

# List of countries to filter
countryList = ["Africa", "Brazil", "Canada", "China", "Germany", "India", "Italy", "Malaysia", "Nepal", "Portugal",
               "Sri Lanka", "United Arab Emirates", "United Kingdom", "United States"]

# Load the data
data = pd.read_csv(Original_dataUri)

# Filter data by countries
filtered_data = data[data["location"].isin(countryList)]

# Delete columns with more than 75% null values
threshold = 0.75 * len(filtered_data)
filtered_data = filtered_data.dropna(axis=1, thresh=threshold)

# Fill remaining empty columns with mean (exclude non-numeric columns)
numeric_columns = filtered_data.select_dtypes(include=np.number).columns
filtered_data[numeric_columns] = filtered_data[numeric_columns].apply(lambda col: col.fillna(col.mean()) if col.isnull().any() else col, axis=0)

# Print the resulting DataFrame
print(filtered_data.head())



