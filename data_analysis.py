import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect('starbucks_stores.db')

# Read the cleaned store location data from the database
query = 'SELECT * FROM store_locations'
df = pd.read_sql_query(query, conn)

# Calculate the total number of Starbucks stores globally
global_store_count = len(df)
print(f"Total number of Starbucks stores globally: {global_store_count}")

# Calculate the number of Starbucks stores by country/region
country_store_count = df['Country'].value_counts()
print("\nNumber of Starbucks stores by country/region:")
print(country_store_count)

# Analyze the distribution of stores across different cities
city_store_count = df['City'].value_counts()
print("\nNumber of Starbucks stores by city:")
print(city_store_count.head(10))  # Display top 10 cities

# Analyze the distribution of stores across different states/provinces
state_store_count = df['StateProvince'].value_counts()
print("\nNumber of Starbucks stores by state/province:")
print(state_store_count.head(10))  # Display top 10 states/provinces

# Identify the top cities with the highest number of Starbucks stores
top_cities = city_store_count.head(10)
print("\nTop 10 cities with the highest number of Starbucks stores:")
print(top_cities)

# Calculate the density of stores per capita in different countries
# (Assuming population data is available in a separate dataset)
population_data = {'US': 328200000, 'CA': 37600000, 'CN': 1393000000, 'JP': 126500000}
store_density = {}
for country, population in population_data.items():
    store_count = country_store_count[country]
    density = store_count / (population / 1000000)  # Stores per million people
    store_density[country] = density

print("\nStarbucks store density per million people:")
for country, density in store_density.items():
    print(f"{country}: {density:.2f}")

# Generate a bar chart of the number of Starbucks stores by country/region
country_store_count.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Country/Region')
plt.ylabel('Number of Starbucks Stores')
plt.title('Number of Starbucks Stores by Country/Region')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Close the database connection
conn.close()