import pandas as pd
import numpy as np

# Load cleaned data
df = pd.read_csv("airbnb_project/airbnb_cleaned.csv")

print("=" * 50)
print("FEATURE ENGINEERING")
print("=" * 50)

# Create new features

# 1. Price categories - Binary
if 'price' in df.columns:
    df['is_expensive'] = np.where(df['price'] > 300, 1, 0)
    print("\nExpensive listings (price > 300):")
    print(df['is_expensive'].value_counts())

    # 2. Price categories (multiple bins)
    price_bins = [0, 100, 200, 300, 500, np.inf]
    price_labels = ['Budget', 'Moderate', 'Premium', 'Luxury', 'Ultra-Luxury']
    df['price_category'] = pd.cut(df['price'], bins=price_bins, labels=price_labels)
    print("\nPrice Categories:")
    print(df['price_category'].value_counts())

# 3. Room type encoding
if 'room type' in df.columns:
    df['room_type_encoded'] = df['room type'].astype('category').cat.codes
    print("\nRoom Type Encoding:")
    print(df[['room type', 'room_type_encoded']].drop_duplicates())

# 4. Neighbourhood group encoding
if 'neighbourhood group' in df.columns:
    df['neighbourhood_encoded'] = df['neighbourhood group'].astype('category').cat.codes
    print("\nNeighbourhood Group Encoding:")
    print(df[['neighbourhood group', 'neighbourhood_encoded']].drop_duplicates())

print("\nNew features created:")
display_cols = ['price']
if 'is_expensive' in df.columns:
    display_cols.append('is_expensive')
if 'price_category' in df.columns:
    display_cols.append('price_category')
if 'room_type_encoded' in df.columns:
    display_cols.append('room_type_encoded')
    
print(df[display_cols].head(10))

# Save featured data
df.to_csv("airbnb_project/airbnb_featured.csv", index=False)
print("\nFeatured data saved to 'airbnb_project/airbnb_featured.csv'")

print("\n" + "=" * 50)
print("FEATURE ENGINEERING COMPLETE")
print("=" * 50)
