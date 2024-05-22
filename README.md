# Starbucks Store Locations Analysis

This project focuses on analyzing the store locations of Starbucks, a popular coffee chain. The project involves data cleaning, data storage, exploratory data analysis, and creating an interactive dashboard to visualize insights about Starbucks store locations worldwide.

## Dataset

The dataset used in this project is the Starbucks store locations dataset, which contains information about Starbucks stores, including their geographic locations, ownership types, and store details. The dataset is obtained in CSV format.

## Project Structure

The project consists of the following files:

- `data_cleaning.py`: Python script for cleaning and preprocessing the dataset.
- `data_storage.py`: Python script for storing the cleaned dataset in a SQLite database.
- `data_analysis.py`: Python script for performing exploratory data analysis on the cleaned dataset.
- `dashboard.py`: Python script for creating an interactive dashboard using Plotly Dash.
- `starbucks_stores.db`: SQLite database file containing the cleaned store locations data.
- `requirements.txt`: File listing the required Python libraries and their versions.

## Prerequisites

To run this project, you need to have the following software installed:

- Python 3.6 or higher
- SQLite

You also need to install the required Python libraries listed in the `requirements.txt` file. You can install them using the following command:

```
pip install -r requirements.txt
```

## Usage

1. Clone this repository to your local machine or download the project files.

2. Ensure that you have the required software and libraries installed.

3. Place the Starbucks store locations dataset CSV file in the project directory.

4. Run the data cleaning script to preprocess the dataset:
   ```
   python data_cleaning.py
   ```

5. Run the data storage script to store the cleaned dataset in a SQLite database:
   ```
   python data_storage.py
   ```

6. Run the data analysis script to perform exploratory data analysis:
   ```
   python data_analysis.py
   ```

7. Run the dashboard script to start the interactive dashboard:
   ```
   python dashboard.py
   ```

8. Open a web browser and navigate to `http://127.0.0.1:8050/` to access the Starbucks Store Locations Dashboard.

## Dashboard Features

The interactive dashboard provides the following features:

- Geographic map displaying the distribution of Starbucks stores worldwide.
- Dropdown selection to filter stores by country.
- Bar chart showing the number of stores by country.
- Pie chart illustrating the proportion of stores by ownership type.
- Heatmap representing store density in different regions.

## Acknowledgments

- The Starbucks store locations dataset used in this project is sourced from [Kaggle](https://www.kaggle.com/starbucks/store-locations).
- This project utilizes various open-source libraries, including Pandas, SQLite, Plotly, and Dash.


