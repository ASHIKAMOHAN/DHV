# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns

# # Original data URI
# Original_dataUri = 'Life-Expectancy-Data-Updated.csv'

# # List of countries to filter
# countryList = ["Belgium", "India", "United Arab Emirates", "Bangladesh", "Brazil", "South Africa", "Kuwait"]

# # Load the data
# data = pd.read_csv(Original_dataUri)

# # Filter data by countries in countryList
# filtered_data = data[data["Country"].isin(countryList)]
# # Get rid of any empty data
# filtered_data.dropna(inplace=True)
# # Save filtered data to CSV
# # filtered_data.to_csv("filtered.csv", index=False)

# # Set the overall figure size
# plt.figure(figsize=(12, 18))

# # Add title space
# plt.subplot(6, 1, 1)  # 6 rows, 1 column, position 1
# plt.text(0.5, 0.5, 'Title of the Combined Image', horizontalalignment='center', verticalalignment='center', fontsize=16, fontweight='bold')
# plt.axis('off')

# # Distribution of infant deaths
# plt.figure(figsize=(8, 6))
# sns.histplot(filtered_data['Infant_deaths'], bins=20, kde=True)
# plt.title('Distribution of Infant Deaths')
# plt.xlabel('Infant Deaths per 1000 Population')
# plt.ylabel('Frequency')
# # plt.show()


# df2000 = filtered_data[filtered_data['Year'] == 2000]
# df2015 = filtered_data[filtered_data['Year'] == 2015]

# # Function to create a bar plot for the top and lowest countries
# def plot_life_expectancy(ax, df, title):
#     top_countries_high = df.nlargest(10, 'Life_expectancy')
#     lowest_countries = df.nsmallest(10, 'Life_expectancy')
#     combined_df = pd.concat([top_countries_high, lowest_countries])

#     # Plot the data for highest life expectancy
#     ax.barh(combined_df['Country'][:10], combined_df['Life_expectancy'][:10], color='skyblue', label='Lowest')

#     # Plot the data for lowest life expectancy
#     ax.barh(combined_df['Country'][10:], combined_df['Life_expectancy'][10:], color='orange', label='Highest')

#     ax.set_title(title)
#     ax.set_xlabel('Life Expectancy')
#     ax.set_ylabel('Country')
#     ax.legend(title='Life Expectancy')

# # Create subplots
# fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8, 10))

# # Plot for 2000
# plot_life_expectancy(axes[0], df2000, 'Top 10 Countries with Highest and Lowest Life Expectancy (Year 2000)')

# # Plot for 2015
# plot_life_expectancy(axes[1], df2015, 'Top 10 Countries with Highest and Lowest Life Expectancy (Year 2015)')

# plt.tight_layout()
# # plt.show()

# def groupedBarPlot(filtered_data):
#     # Filter years from 2000 to 2015 with a skip of 5 years
#     years_to_plot = np.arange(2000, 2016, 5)

#     # Filter data for selected years
#     filtered_data_subset = filtered_data[filtered_data['Year'].isin(years_to_plot)]

#     # Create a grouped barplot
#     plt.figure(figsize=(12, 8))
#     sns.barplot(x='Year', y='GDP_per_capita', hue='Country', data=filtered_data_subset, palette='Set1')

#     # Adding labels and  title
#     plt.xlabel('Year')
#     plt.ylabel('GDP_per_capita')
#     plt.title('Grouped Barplot of GDP_per_capita Over the Years')
#     plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')

#     # Display the plot
#     plt.tight_layout()
#     # plt.show()

# # Call the groupedBarPlot function with your filtered data
# groupedBarPlot(filtered_data)


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Original data URI
Original_dataUri = 'Life-Expectancy-Data-Updated.csv'

# List of countries to filter
countryList = ["Africa", "North America", "South America", "Asia", "Middle East"]

# Load the data
data = pd.read_csv(Original_dataUri)

# Filter data by countries in countryList
filtered_data = data[data["Region"].isin(countryList)]
# Get rid of any empty data
filtered_data.dropna(inplace=True)
# Save filtered data to CSV
filtered_data.to_csv("filtered.csv", index=False)

# Distribution of infant deaths
plt.figure(figsize=(8, 6))
sns.histplot(filtered_data['Infant_deaths'], bins=20, kde=True)
plt.title('Distribution of Infant Deaths')
plt.xlabel('Infant Deaths per 1000 Population')
plt.ylabel('Frequency')
plt.show()

def groupedBarPlot(filtered_data):
    # Filter years from 2000 to 2015 with a skip of 5 years
    years_to_plot = np.arange(2000, 2016, 5)

    # Filter data for selected years
    filtered_data_subset = filtered_data[filtered_data['Year'].isin(years_to_plot)]

    # Create a grouped barplot
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Year', y='GDP_per_capita', hue='Region', data=filtered_data_subset, palette='Set1',ci=None)

    # Adding labels and  title
    plt.xlabel('Year')
    plt.ylabel('GDP_per_capita')
    plt.title('Grouped Barplot of GDP_per_capita Over the Years')
    plt.legend(title='Region', bbox_to_anchor=(1.05, 1), loc='upper left')

    # Display the plot
    plt.tight_layout()
    plt.show()

# Call the groupedBarPlot function with your filtered data
groupedBarPlot(filtered_data)


