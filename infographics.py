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
# # Save filtered data to CSV
# # filtered_data.to_csv("filtered.csv", index=False)

# # Visualize life expectancy over the years
# plt.figure(figsize=(10, 6))
# sns.lineplot(x='Year', y='Life_expectancy', data=filtered_data, hue='Region')
# plt.title('Life Expectancy Over the Years by Region')
# plt.xlabel('Year')
# plt.ylabel('Life Expectancy')
# plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
# plt.show()

# # Distribution of infant deaths
# plt.figure(figsize=(8, 6))
# sns.histplot(filtered_data['Infant_deaths'], bins=20, kde=True)
# plt.title('Distribution of Infant Deaths')
# plt.xlabel('Infant Deaths per 1000 Population')
# plt.ylabel('Frequency')
# plt.show()


# plt.figure(figsize=(10, 6))
# sns.barplot(x='Region', y='Life_expectancy', data=filtered_data, palette="Set2")
# plt.title('Average Life Expectancy by Region')
# plt.xlabel('Region')
# plt.ylabel('Average Life Expectancy')
# plt.show()


df2000 = filtered_data[filtered_data['Year'] == 2000]
df2015 = filtered_data[filtered_data['Year'] == 2015]

# Function to create a bar plot for the top and lowest countries
def plot_life_expectancy(ax, df, title):
    top_10_countries_high = df.nlargest(10, 'Life_expectancy')
    lowest_10_countries = df.nsmallest(10, 'Life_expectancy')
    combined_df = pd.concat([top_10_countries_high, lowest_10_countries])

    # Plot the data for highest life expectancy
    ax.barh(combined_df['Country'][:10], combined_df['Life_expectancy'][:10], color='skyblue', label='Highest')

    # Plot the data for lowest life expectancy
    ax.barh(combined_df['Country'][10:], combined_df['Life_expectancy'][10:], color='orange', label='Lowest')

    ax.set_title(title)
    ax.set_xlabel('Life Expectancy')
    ax.set_ylabel('Country')
    ax.legend(title='Life Expectancy')

# Create subplots
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8, 10))

# Plot for 2000
plot_life_expectancy(axes[0], df2000, 'Top 10 Countries with Highest and Lowest Life Expectancy (Year 2000)')

# Plot for 2015
plot_life_expectancy(axes[1], df2015, 'Top 10 Countries with Highest and Lowest Life Expectancy (Year 2015)')

plt.tight_layout()
plt.show()

def barGraph(filtered_data):
	plt.figure(figsize=(10, 6))
	filtered_data.plot(kind='bar', width=0.8,  ax=plt.gca())

	# Adding labels and title
	plt.xlabel('Year')
	plt.ylabel('Happiness Index')
	plt.title('Happiness Index by Country for 2015 - 2020')
	plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')

	# Display the plot
	plt.tight_layout()
	plt.show()