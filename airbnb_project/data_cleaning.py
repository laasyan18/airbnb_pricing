import pandas as pd
import numpy as np

# Load data
df = pd.read_csv("Airbnb_Open_Data.csv")

print("=" * 50)
print("DATA CLEANING")
print("=" * 50)

# Initial shape
print(f"\nInitial dataset shape: {df.shape}")

# Handle missing values
print(f"\nMissing values before cleaning:")
print(df.isnull().sum())

# Drop rows with missing price (if price column exists)
if 'price' in df.columns:
    df = df.dropna(subset=['price'])
    print(f"\nRows after removing missing prices: {len(df)}")

# Fill other missing values if needed
# Example: df['column_name'].fillna(df['column_name'].median(), inplace=True)

print(f"\nMissing values after cleaning:")
print(df.isnull().sum())

# Remove duplicates
initial_count = len(df)
df = df.drop_duplicates()
print(f"\nDuplicates removed: {initial_count - len(df)}")

# Data type conversions
if 'price' in df.columns:
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df = df.dropna(subset=['price'])  # Remove rows where price couldn't be converted

print(f"\nFinal dataset shape: {df.shape}")

# Save cleaned data
df.to_csv("airbnb_project/airbnb_cleaned.csv", index=False)
print("\nCleaned data saved to 'airbnb_project/airbnb_cleaned.csv'")

print("\n" + "=" * 50)
print("CLEANING COMPLETE")
print("=" * 50)
