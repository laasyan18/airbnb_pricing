import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load data
df = pd.read_csv("airbnb_project/airbnb_featured.csv")

print("=" * 50)
print("DATA VISUALIZATION")
print("=" * 50)

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (15, 12)

# Create subplots
fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle('Airbnb Data Analysis Dashboard', fontsize=20, fontweight='bold')

# 1. Price Distribution
if 'price' in df.columns:
    # Remove extreme outliers for better visualization
    price_data = df[df['price'] < df['price'].quantile(0.95)]['price']
    axes[0, 0].hist(price_data, bins=50, color='skyblue', edgecolor='black')
    axes[0, 0].set_title('Price Distribution (95th percentile)', fontsize=14, fontweight='bold')
    axes[0, 0].set_xlabel('Price ($)')
    axes[0, 0].set_ylabel('Frequency')

# 2. Room Type Distribution
if 'room type' in df.columns:
    room_counts = df['room type'].value_counts()
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#ff99cc']
    axes[0, 1].bar(room_counts.index, room_counts.values, color=colors[:len(room_counts)])
    axes[0, 1].set_title('Room Type Distribution', fontsize=14, fontweight='bold')
    axes[0, 1].set_xlabel('Room Type')
    axes[0, 1].set_ylabel('Count')
    axes[0, 1].tick_params(axis='x', rotation=45)

# 3. Neighbourhood Group Pie Chart
if 'neighbourhood group' in df.columns:
    neighbourhood_counts = df['neighbourhood group'].value_counts()
    axes[0, 2].pie(neighbourhood_counts, labels=neighbourhood_counts.index, autopct='%1.1f%%', startangle=90)
    axes[0, 2].set_title('Neighbourhood Group Distribution', fontsize=14, fontweight='bold')
else:
    axes[0, 2].text(0.5, 0.5, 'No neighbourhood data', ha='center', va='center')

# 4. Price by Room Type - Box Plot
if 'price' in df.columns and 'room type' in df.columns:
    # Filter outliers for better visualization
    price_filtered = df[df['price'] < df['price'].quantile(0.95)]
    price_filtered.boxplot(column='price', by='room type', ax=axes[1, 0])
    axes[1, 0].set_title('Price by Room Type (95th percentile)', fontsize=14, fontweight='bold')
    axes[1, 0].set_xlabel('Room Type')
    axes[1, 0].set_ylabel('Price ($)')
    plt.sca(axes[1, 0])
    plt.xticks(rotation=45)

# 5. Price Category Distribution
if 'price_category' in df.columns:
    price_cat_counts = df['price_category'].value_counts().sort_index()
    axes[1, 1].bar(price_cat_counts.index.astype(str), price_cat_counts.values, color='coral', edgecolor='black')
    axes[1, 1].set_title('Price Category Distribution', fontsize=14, fontweight='bold')
    axes[1, 1].set_xlabel('Category')
    axes[1, 1].set_ylabel('Count')
    axes[1, 1].tick_params(axis='x', rotation=45)
else:
    axes[1, 1].text(0.5, 0.5, 'No price category data', ha='center', va='center')

# 6. Expensive vs Non-Expensive
if 'is_expensive' in df.columns:
    expensive_counts = df['is_expensive'].value_counts()
    labels = ['Not Expensive (<$300)', 'Expensive (>$300)']
    axes[1, 2].pie(expensive_counts, labels=labels, autopct='%1.1f%%', 
                   colors=['lightgreen', 'salmon'], startangle=90)
    axes[1, 2].set_title('Expensive Listings Distribution', fontsize=14, fontweight='bold')
else:
    axes[1, 2].text(0.5, 0.5, 'No expensive classification', ha='center', va='center')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('airbnb_project/airbnb_analysis_dashboard.png', dpi=300, bbox_inches='tight')
print("\nVisualizations saved to 'airbnb_project/airbnb_analysis_dashboard.png'")
plt.show()

print("\n" + "=" * 50)
print("VISUALIZATION COMPLETE")
print("=" * 50)
