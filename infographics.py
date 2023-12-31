

# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns

# Original_dataUri = 'Life-Expectancy-Data-Updated.csv'
# data = pd.read_csv(Original_dataUri)

# countryList = ["Africa", "North America", "South America", "Asia", "Middle East"]
# region_colors = {
#     'Africa': 'blue',
#     'North America': 'green',
#     'South America': 'red',
#     'Asia': 'purple',
#     'Middle East': 'orange'
# }
# filtered_data = data[data["Region"].isin(countryList)]
# filtered_data.dropna(inplace=True)
# filtered_data.to_csv("filtered.csv", index=False)
# years_to_plot = np.arange(2000, 2016, 5)
# filtered_data_subset = filtered_data[filtered_data['Year'].isin(years_to_plot)]
# grouped_df = filtered_data.groupby('Region')[['Under_five_deaths', 'Infant_deaths']].sum().reset_index()
# filtered_df = filtered_data.sort_values(by='Population_mln', ascending=False)

# plt.figure(figsize=(16, 16))  # Overall figure size

# # First subplot: Title space
# plt.subplot(3, 2, 1)  # 3 rows, 2 columns, position 1
# plt.text(0.5, 0.5, 'Life Expectancy 2000 - 2015', horizontalalignment='center', verticalalignment='center', fontsize=16, fontweight='bold')
# plt.axis('off')

# # Plotting grouped barchart
# plt.subplot(3, 2, 3)
# sns.barplot(x='Year', y='GDP_per_capita', hue='Region', data=filtered_data_subset,color=[region_colors[region] for region in filtered_df['Region']], ci=None)
# plt.xlabel('Year')
# plt.ylabel('GDP_per_capita')
# plt.title('Grouped Barplot of GDP_per_capita Over the Years')
# plt.legend(title='Region', bbox_to_anchor=(1.05, 1), loc='upper left')

# # Increase the size of the pie chart subplot
# pie_ax = plt.subplot(3, 2, 4, aspect='equal')  # 3 rows, 2 columns, position 4
# pie_ax.pie(grouped_df['Under_five_deaths'], labels=grouped_df['Region'], autopct='%1.1f%%', startangle=140, color=[region_colors[region] for region in filtered_df['Region']])
# pie_ax.set_title('Under-Five Deaths by Region')

# # Plotting line chart
# plt.subplot(3, 2, 5)
# sns.lineplot(x='Year', y='Life_expectancy', hue='Region', data=filtered_data, palette='Set1', marker='o')
# plt.xlabel('Year')
# plt.ylabel('Life Expectancy')
# plt.title('Life Expectancy Over the Years by Region')
# plt.legend(title='Region', bbox_to_anchor=(1.05, 1), loc='upper left')

# # Plotting horizontal bar chart
# plt.subplot(3, 2, 6)
# plt.barh(filtered_df['Region'], filtered_df['Population_mln'], color=[region_colors[region] for region in filtered_df['Region']], alpha=0.7)
# plt.xlabel("Population [in Millions]")
# plt.ylabel("Region")
# plt.title("Population Distribution by Region")

# # Adjust layout and save the figure
# plt.tight_layout(pad=4.0, h_pad=6.0, w_pad=2.0)
# plt.subplots_adjust(wspace=0.8, hspace=0.6)
# plt.savefig('combined_plots.png', dpi=300)  # Save as PNG file with higher resolution (dpi)

# plt.show()

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

Original_dataUri = 'Life-Expectancy-Data-Updated.csv'
data = pd.read_csv(Original_dataUri)

countryList = ["Africa", "North America", "South America", "Asia", "Middle East"]
region_colors = {
    'Africa': 'blue',
    'North America': 'green',
    'South America': 'red',
    'Asia': 'purple',
    'Middle East': 'orange'
}
filtered_data = data[data["Region"].isin(countryList)]
filtered_data.dropna(inplace=True)
filtered_data.to_csv("filtered.csv", index=False)
years_to_plot = np.arange(2000, 2016, 5)
filtered_data_subset = filtered_data[filtered_data['Year'].isin(years_to_plot)]
grouped_df = filtered_data.groupby('Region')[['Under_five_deaths', 'Infant_deaths']].sum().reset_index()
filtered_df = filtered_data.sort_values(by='Population_mln', ascending=False)

plt.figure(figsize=(16, 16))  # Overall figure size

# First subplot: Title space
plt.subplot(3, 2, 1)  # 3 rows, 2 columns, position 1
plt.text(0.5, 0.5, 'Life Expectancy 2000 - 2015', horizontalalignment='center', verticalalignment='center', fontsize=16, fontweight='bold')
plt.axis('off')

# Plotting grouped barchart
plt.subplot(3, 2, 3)
sns.barplot(x='Year', y='GDP_per_capita', hue='Region', data=filtered_data_subset, palette=region_colors, ci=None)
plt.xlabel('Year')
plt.ylabel('GDP_per_capita')
plt.title('Grouped Barplot of GDP_per_capita Over the Years')
plt.legend(title='Region', bbox_to_anchor=(1.05, 1), loc='upper left')

pie_ax = plt.subplot(3, 2, 4, aspect='equal')  # 3 rows, 2 columns, position 4
pie_ax.pie(grouped_df['Under_five_deaths'], labels=grouped_df['Region'], autopct='%1.1f%%', startangle=140, colors=[region_colors[region] for region in grouped_df['Region']])
pie_ax.set_title('Under-Five Deaths by Region')

# Plotting line chart
plt.subplot(3, 2, 5)
sns.lineplot(x='Year', y='Life_expectancy', hue='Region', data=filtered_data, palette=region_colors, marker='o')
plt.xlabel('Year')
plt.ylabel('Life Expectancy')
plt.title('Life Expectancy Over the Years by Region')
plt.legend(title='Region', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.subplot(3, 2, 6)
plt.barh(filtered_df['Region'], filtered_df['Population_mln'], color=region_colors, alpha=0.7)
plt.xlabel("Population [in Millions]")
plt.ylabel("Region")
plt.title("Population Distribution by Region")
plt.show()

# Adjust layout and save the figure
plt.tight_layout(pad=4.0, h_pad=6.0, w_pad=2.0)
plt.subplots_adjust(wspace=0.8, hspace=0.6)
plt.savefig('combined_plots.png', dpi=300)  # Save as PNG file with higher resolution (dpi)

plt.show()

