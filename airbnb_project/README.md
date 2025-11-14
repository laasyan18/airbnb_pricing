# Airbnb Data Science & Visualization Project

## Project Overview
This project analyzes Airbnb Open Data to extract insights about pricing, room types, and neighborhood distributions using data science and visualization techniques.

## 📁 Files Structure
```
airbnb_project/
│
├── data_exploration.py       # Initial data exploration and understanding
├── data_cleaning.py          # Data cleaning and preprocessing
├── feature_engineering.py    # Creating new features
├── visualization.py          # Data visualizations and dashboard
├── statistical_analysis.py   # Statistical tests and analysis
├── airbnb_cleaned.csv        # Cleaned dataset (generated)
├── airbnb_featured.csv       # Dataset with engineered features (generated)
├── airbnb_analysis_dashboard.png  # Visualization dashboard (generated)
└── README.md                 # This file
```

## 🎯 Project Objectives
1. **Data Exploration**: Understand the structure and characteristics of Airbnb listings
2. **Data Cleaning**: Handle missing values, duplicates, and data quality issues
3. **Feature Engineering**: Create meaningful features for analysis
4. **Visualization**: Create compelling visualizations to communicate insights
5. **Statistical Analysis**: Perform statistical tests and identify patterns

## 🔍 Key Findings
1. **Price Analysis**: 
   - Analysis of pricing patterns across different room types
   - Identification of price categories (Budget, Moderate, Premium, Luxury, Ultra-Luxury)
   
2. **Room Type Distribution**: 
   - Distribution of listings by room type
   - Price comparison across room types

3. **Neighborhood Analysis**: 
   - Geographic distribution of listings
   - Neighborhood group pricing patterns

4. **Price Categories**: 
   - Classification of listings into price segments
   - Expensive vs non-expensive listings (threshold: $300)

## 🚀 How to Run
1. **Install Required Libraries**:
   ```bash
   pip install pandas numpy matplotlib seaborn scipy scikit-learn
   ```

2. **Run the Scripts in Order**:
   ```bash
   # Step 1: Explore the data
   python data_exploration.py
   
   # Step 2: Clean the data
   python data_cleaning.py
   
   # Step 3: Create features
   python feature_engineering.py
   
   # Step 4: Generate visualizations
   python visualization.py
   
   # Step 5: Perform statistical analysis
   python statistical_analysis.py
   ```

## 📊 Visualizations
The project generates a comprehensive dashboard including:
- Price distribution histogram
- Room type bar chart
- Neighbourhood group pie chart
- Price by room type box plot
- Price category distribution
- Expensive vs non-expensive pie chart

## 🛠️ Technologies Used
- **Python 3.x**: Programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical operations
- **Matplotlib**: Data visualization
- **Seaborn**: Statistical data visualization
- **SciPy**: Statistical analysis
- **Scikit-learn**: Machine learning utilities

## 📈 Statistical Methods Applied
- Descriptive statistics (mean, median, mode, std dev)
- Correlation analysis
- Hypothesis testing (t-tests)
- Outlier detection (IQR method)
- Quartile analysis

## 💡 Insights & Applications
This analysis can help:
- **Hosts**: Set competitive pricing for their listings
- **Guests**: Understand pricing patterns and find good deals
- **Analysts**: Identify market trends and patterns
- **Investors**: Make data-driven decisions about property investments

## 📝 Data Source
Airbnb Open Data (Airbnb_Open_Data.csv)
