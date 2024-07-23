import pandas as pd

# Load dataset from CSV and remove rows with null values
df = pd.read_csv('movies.csv').dropna()

print(df.head())  # Print first few rows to verify data
