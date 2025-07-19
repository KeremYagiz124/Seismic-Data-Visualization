# Earthquake Data Analysis and Visualization

This repository contains a project that analyzes earthquake data and visualizes the results using Python. The dataset used contains earthquake records with attributes such as date, time, location, magnitude, and depth.

## Steps Included in the Project:
- **Data Loading & Preprocessing**: The dataset (`earthquake_data.xlsx`) is loaded, and columns like date and time are combined to create a unified timestamp. Missing values in the Magnitude column are cleaned up.
- **Statistical Analysis**: Basic statistics (counts, means, and distributions) are provided. Missing values in the `Magnitude (ML)` column are checked, and rows with missing values are removed.
- **Visualization**:
  - A plot showing the number of earthquakes per day.
  - A histogram displaying the distribution of earthquake magnitudes.
  - A scatter plot showing the relationship between depth and magnitude, colored by location.
- **Mapping Earthquakes**: A geographic visualization of earthquakes is created using **Folium**. Each earthquake is plotted on an interactive map with markers proportional to the earthquake's magnitude. The map is saved as an HTML file (`earthquakes_map.html`).

## Key Files:
- `earthquake_data.xlsx`: The dataset containing earthquake records.
- `earthquakes_map.html`: An interactive map visualizing the locations and magnitudes of earthquakes.

## Libraries Used:
- `Pandas` for data manipulation
- `Matplotlib`, `Seaborn` for data visualization
- `Folium` for creating the interactive map

## Instructions for Running the Project:

1. Install the required libraries:
   ```bash
   pip install pandas matplotlib seaborn folium
