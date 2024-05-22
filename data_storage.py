import sqlite3
import pandas as pd

# Connect to a SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('starbucks_stores.db')

# Read the cleaned store locations dataset
df = pd.read_csv('cleaned_store_locations.csv')

# Create a table to store the cleaned store location data
create_table_query = '''
    CREATE TABLE IF NOT EXISTS store_locations (
        rand TEXT,
        StoreNumber INTEGER,
        StoreName TEXT,
        OwnershipType TEXT,
        StreetAddress TEXT,
        City TEXT,
        StateProvince TEXT,
        Country TEXT,
        Postcode TEXT,
        PhoneNumber TEXT,
        Timezone TEXT,
        Longitude REAL,
        Latitude REAL
    )
'''
conn.execute(create_table_query)

# Insert the cleaned data into the table
df.to_sql('store_locations', conn, if_exists='replace', index=False)

# Commit the changes and close the connection
conn.commit()
conn.close()
