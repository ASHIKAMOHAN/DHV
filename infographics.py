import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Read the data
Original_dataUri = 'Life-Expectancy-Data-Updated.csv'
data = pd.read_csv(Original_dataUri)

# Define region colors
region_colors = {
    'Africa': '#58508d',
    'North America': '#ff6361',
    'South America': '#bc5090',
    'Asia': '#ffa600',
    'Middle East': '#003f5c'
}

# Filter and clean data
Region = ["Africa", "North America", "South America", "Asia", "Middle East"]
filtered_data = data[data["Region"].isin(Region)].dropna()
filtered_data.to_csv("filtered.csv", index=False)

# Subset data for specific years
years_to_plot = np.arange(2000, 2016, 5)
filtered_data_subset = filtered_data[filtered_data['Year'].isin(years_to_plot)]

# Grouped DataFrame
grouped_df = filtered_data.groupby('Region')[['Under_five_deaths', 'Infant_deaths']].sum().reset_index()
filtered_df = filtered_data.sort_values(by='Population_mln', ascending=False)

# Set up the subplots with a background color
fig, axes = plt.subplots(2, 2, figsize=(15, 10), facecolor='#fceee9')  # Set the background color here

# Title space for the description
fig.suptitle('Infographic: Life Expectancy Analysis', fontsize=18, y=1.02)

# Grouped barchart
sns.barplot(x='Year', y='GDP_per_capita', hue='Region', data=filtered_data_subset, palette=region_colors, errorbar=None, ax=axes[0, 0])
axes[0, 0].set_xlabel('Year')
axes[0, 0].set_ylabel('GDP_per_capita')
axes[0, 0].set_title('Grouped Barplot of GDP_per_capita Over the Years')
axes[0, 0].legend().set_visible(False)  # Remove legend

# Piechart
explode = (0.1, 0, 0, 0, 0)
wedges, texts, autotexts = axes[0, 1].pie(grouped_df['Under_five_deaths'], labels=None, autopct='%1.1f%%',
                                           startangle=140, colors=[region_colors[region] for region in grouped_df['Region']],
                                           pctdistance=1.15, explode=explode)  # Increase pctdistance to move the percentages outside
axes[0, 1].set_title('Under-Five Deaths by Region')

# Move the percentage labels outside the pie chart
for autotext in autotexts:
    autotext.set_horizontalalignment('center')  # Center the labels inside the wedges
    autotext.set_verticalalignment('center')  # Center the labels inside the wedges


# Line chart
sns.lineplot(x='Year', y='Life_expectancy', hue='Region', data=filtered_data, palette=region_colors, marker='o', ax=axes[1, 0])
axes[1, 0].set_xlabel('Year')
axes[1, 0].set_ylabel('Life Expectancy')
axes[1, 0].set_title('Life Expectancy Over the Years by Region')
axes[1, 0].legend().set_visible(False)  # Remove legend

# Horizontal bargraph
axes[1, 1].barh(filtered_df['Region'], filtered_df['Population_mln'], color=[region_colors[region] for region in filtered_df['Region']], alpha=0.7)
axes[1, 1].set_xlabel("Population [in Millions]")
axes[1, 1].set_ylabel("Region")
axes[1, 1].set_title("Population Distribution by Region")

# Add common legend between the first and second rows with a transparent background
legend = fig.legend(handles, labels, loc='upper center', title='Region', bbox_to_anchor=(0.5, 0.5), ncol=5, facecolor='white', framealpha=1, edgecolor='none')  # Set edgecolor to 'none' to remove legend outline

# Remove the spines (outlines) from the subplots
for ax in axes.flatten():
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 1])  # Ensure there's space for the title
plt.subplots_adjust(hspace=0.8)  # Adjust vertical space between subplots

# Add a description column
fig.text(0.3, -0.05, 'Description: This infographic visualizes GDP per capita, under-five deaths, and life expectancy over the years for different regions.', ha='center', va='center', fontsize=10)

# Save the plot as PNG with a transparent background
plt.savefig("your-student-id.png", dpi=300, transparent=True)
plt.show()