import pandas as pd
import numpy as np
from scipy import stats

# Load data
df = pd.read_csv("airbnb_project/airbnb_featured.csv")

print("=" * 50)
print("STATISTICAL ANALYSIS")
print("=" * 50)

# Descriptive Statistics
if 'price' in df.columns:
    print("\n1. DESCRIPTIVE STATISTICS")
    print("-" * 50)
    print("\nPrice Statistics:")
    print(f"Mean: ${df['price'].mean():.2f}")
    print(f"Median: ${df['price'].median():.2f}")
    print(f"Mode: ${df['price'].mode().iloc[0]:.2f}")
    print(f"Std Dev: ${df['price'].std():.2f}")
    print(f"Min: ${df['price'].min():.2f}")
    print(f"Max: ${df['price'].max():.2f}")
    print(f"Range: ${df['price'].max() - df['price'].min():.2f}")
    
    # Quartiles
    print(f"\n25th Percentile: ${df['price'].quantile(0.25):.2f}")
    print(f"50th Percentile (Median): ${df['price'].quantile(0.50):.2f}")
    print(f"75th Percentile: ${df['price'].quantile(0.75):.2f}")

# Correlation Analysis
print("\n2. CORRELATION ANALYSIS")
print("-" * 50)
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
if len(numeric_cols) > 1:
    correlation_matrix = df[numeric_cols].corr()
    print("\nCorrelation Matrix:")
    print(correlation_matrix)
    
    # Find strong correlations
    print("\nStrong Correlations (|r| > 0.5):")
    for i in range(len(correlation_matrix.columns)):
        for j in range(i+1, len(correlation_matrix.columns)):
            corr_val = correlation_matrix.iloc[i, j]
            if abs(corr_val) > 0.5:
                print(f"{correlation_matrix.columns[i]} <-> {correlation_matrix.columns[j]}: {corr_val:.3f}")

# Hypothesis Testing - Price by Room Type
if 'price' in df.columns and 'room type' in df.columns:
    print("\n3. HYPOTHESIS TESTING")
    print("-" * 50)
    room_types = df['room type'].unique()
    if len(room_types) >= 2:
        group1 = df[df['room type'] == room_types[0]]['price'].dropna()
        group2 = df[df['room type'] == room_types[1]]['price'].dropna()
        
        if len(group1) > 0 and len(group2) > 0:
            t_stat, p_value = stats.ttest_ind(group1, group2)
            print(f"\nT-test: {room_types[0]} vs {room_types[1]}")
            print(f"Mean {room_types[0]}: ${group1.mean():.2f}")
            print(f"Mean {room_types[1]}: ${group2.mean():.2f}")
            print(f"T-statistic: {t_stat:.4f}")
            print(f"P-value: {p_value:.4f}")
            
            if p_value < 0.05:
                print("Result: Significant difference in prices (α = 0.05)")
            else:
                print("Result: No significant difference in prices (α = 0.05)")

# Outlier Detection
if 'price' in df.columns:
    print("\n4. OUTLIER DETECTION (IQR Method)")
    print("-" * 50)
    Q1 = df['price'].quantile(0.25)
    Q3 = df['price'].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = df[(df['price'] < lower_bound) | (df['price'] > upper_bound)]
    
    print(f"\nQ1 (25th percentile): ${Q1:.2f}")
    print(f"Q3 (75th percentile): ${Q3:.2f}")
    print(f"IQR: ${IQR:.2f}")
    print(f"Lower bound: ${lower_bound:.2f}")
    print(f"Upper bound: ${upper_bound:.2f}")
    print(f"\nNumber of outliers detected: {len(outliers)}")
    print(f"Percentage of outliers: {(len(outliers)/len(df))*100:.2f}%")

# Summary by Category
if 'price_category' in df.columns and 'price' in df.columns:
    print("\n5. SUMMARY BY PRICE CATEGORY")
    print("-" * 50)
    category_summary = df.groupby('price_category')['price'].agg([
        ('count', 'count'),
        ('mean', 'mean'),
        ('median', 'median'),
        ('std', 'std'),
        ('min', 'min'),
        ('max', 'max')
    ])
    print(category_summary)

print("\n" + "=" * 50)
print("STATISTICAL ANALYSIS COMPLETE")
print("=" * 50)
