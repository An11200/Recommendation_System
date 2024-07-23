import pandas as pd

# Assuming 'data.csv' is your original dataset file
input_file = 'movies_metadata.csv'
output_file = 'filtered_data.csv'

# Define column data types to avoid DtypeWarning
dtype_dict = {'overview': str}  # Replace 'overview' with actual problematic column name if different

# Read the original dataset into a DataFrame
df = pd.read_csv(input_file, dtype=dtype_dict)

# Extracting only title and genres
filtered_data = df[['title', 'genres','vote_average']]

# Expand genres into separate rows
filtered_data = filtered_data.explode('genres')

# Write the filtered data to a new CSV file
filtered_data.to_csv(output_file, index=False)

print(f"Filtered data saved to {output_file}")

