import pandas as pd

# Read the store locations dataset into a DataFrame
df = pd.read_csv('directory.csv')

# Handling missing values
# Option 1: Drop rows with missing values
df.dropna(subset=['Phone Number', 'Postcode'], inplace=True)
# Option 2: Fill missing values with appropriate values
df.fillna({'Phone Number': 'Unknown', 'Postcode': 'Unknown'}, inplace=True)

# Removing duplicates
df.drop_duplicates(subset=['Store Number'], inplace=True)

# Converting data types if necessary
df['Store Number'] = df['Store Number'].str.split('-').str[0].astype(int)  # Extract store number and convert to integer type
df['Longitude'] = df['Longitude'].astype(float)
df['Latitude'] = df['Latitude'].astype(float)

# Renaming columns for consistency
df.rename(columns={'State/Province': 'StateProvince', 'Phone Number': 'PhoneNumber'}, inplace=True)

# Save the cleaned dataset to a new file
df.to_csv('cleaned_store_locations.csv', index=False)