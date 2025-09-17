import pandas as pd

# Load dataset
df = pd.read_csv('metadata.csv')

# Basic exploration
print(df.shape)          # Rows x Columns
print(df.info())         # Data types
print(df.head())         # First 5 rows
print(df.isnull().sum()) # Missing values per column
print(df.describe())     # Summary statistics for numerical data
