import pandas as pd
import numpy as np

# Load Airbnb data
df = pd.read_csv("Airbnb_Open_Data.csv")

# Data Exploration
print("=" * 50)
print("AIRBNB DATA EXPLORATION")
print("=" * 50)

print("\nDataset Shape:", df.shape)
print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 rows:")
print(df.head())

print("\nBasic Statistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

if 'room type' in df.columns:
    print("\nRoom Type Distribution:")
    print(df['room type'].value_counts())

if 'neighbourhood group' in df.columns:
    print("\nNeighbourhood Group Distribution:")
    print(df['neighbourhood group'].value_counts())

print("\n" + "=" * 50)
print("EXPLORATION COMPLETE")
print("=" * 50)
