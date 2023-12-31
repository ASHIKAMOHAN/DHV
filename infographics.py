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

# Define the missing function
def pie_chart_health_metrics(ax, df, metric, title):
    # Group the data by region and sum the selected metric
    grouped_df = df.groupby('Region')[metric].sum().reset_index()

    # Plot a pie chart
    ax.pie(grouped_df[metric], labels=grouped_df['Region'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
    ax.set_title(title)

# Define the groupedBarPlot function
def groupedBarPlot(ax, df):
    # Filter years from 2000 to 2015 with a skip of 5 years
    years_to_plot = np.arange(2000, 2016, 5)

    # Filter data for selected years
    filtered_data_subset = df[df['Year'].isin(years_to_plot)]

    # Create a grouped barplot
    sns.barplot(x='Year', y='GDP_per_capita', hue='Region', data=filtered_data_subset, palette='Set1', ci=None, ax=ax)

    # Adding labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('GDP_per_capita')
    ax.set_title('Grouped Barplot of GDP_per_capita Over the Years')
    ax.legend(title='Region', bbox_to_anchor=(1.05, 1), loc='upper left')

# Define the horizontalBarPlot function
def horizontalBarPlot(ax, df):
    # Sort data by population in descending order
    df = df.sort_values(by='Population_mln', ascending=False)

    # Define custom colors for each region
    region_colors = {
        'Africa': 'blue',
        'North America': 'green',
        'South America': 'red',
        'Asia': 'purple',
        'Middle East': 'orange'
    }

    # Create a horizontal bar plot with different colors for each region
    ax.barh(df['Region'], df['Population_mln'], color=[region_colors[region] for region in df['Region']], alpha=0.7)

    ax.set_xlabel("Population [in Millions]")
    ax.set_ylabel("Region")
    ax.set_title("Population Distribution by Region")

# Create a figure with 2 rows and 4 columns
fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(20, 12))

# First column: Grouped Bar Plot
groupedBarPlot(axes[0, 0], filtered_data)
axes[0, 0].set_facecolor(sns.color_palette('pastel')[0])  # Set background color to pastel

# Second column: Pie chart for under-five deaths
pie_chart_health_metrics(axes[0, 1], filtered_data, 'Under_five_deaths', 'Under-Five Deaths by Region')
axes[0, 1].set_facecolor(sns.color_palette('pastel')[1])  # Set background color to pastel

# Third column: Pie chart for infant deaths
pie_chart_health_metrics(axes[0, 2], filtered_data, 'Infant_deaths', 'Infant Deaths by Region')
axes[0, 2].set_facecolor(sns.color_palette('pastel')[2])  # Set background color to pastel

# Fourth column: Line plot for life expectancy
sns.lineplot(x='Year', y='Life_expectancy', hue='Region', data=filtered_data, palette='Set1', marker='o', ax=axes[0, 3])
axes[0, 3].set_facecolor(sns.color_palette('pastel')[3])  # Set background color to pastel

# Fifth column: Horizontal bar plot for population distribution
horizontalBarPlot(axes[1, 0], filtered_data)
axes[1, 0].set_facecolor(sns.color_palette('pastel')[4])  # Set background color to pastel

# Sixth column: Description for Grouped Bar Plot
axes[1, 1].text(0.5, 0.5, "This plot shows the GDP per capita over the years for different regions.", 
                horizontalalignment='center', verticalalignment='center', fontsize=12)
axes[1, 1].axis('off')
axes[1, 1].set_facecolor(sns.color_palette('pastel')[5])  # Set background color to pastel

# Seventh column: Description for Pie Charts
axes[1, 2].text(0.5, 0.5, "These pie charts represent the distribution of under-five deaths and infant deaths by region.", 
                horizontalalignment='center', verticalalignment='center', fontsize=12)
axes[1, 2].axis('off')
axes[1, 2].set_facecolor(sns.color_palette('pastel')[6])  # Set background color to pastel

# Eighth column: Description for Horizontal Bar Plot
axes[1, 3].text(0.5, 0.5, "This plot illustrates the population distribution across regions.", 
                horizontalalignment='center', verticalalignment='center', fontsize=12)
axes[1, 3].axis('off')
axes[1, 3].set_facecolor(sns.color_palette('pastel')[7])  # Set background color to pastel

# Add a title to the entire figure
plt.suptitle("Life Expectancy Over Different Regions (2000-2015) - A Study", fontsize=16, fontweight='bold')

# Save the figure
plt.tight_layout(pad=4.0, h_pad=6.0, w_pad=2.0)
plt.subplots_adjust(wspace=0.8, hspace=0.6) 
plt.savefig('combined_plots_with_description.png', dpi=300)  # Save as PNG file with higher resolution (dpi)

# Show the entire figure
plt.show()
