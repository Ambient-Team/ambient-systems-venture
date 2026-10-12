# AI Script to Improve Fleet Utilization Rate
# Description:
# This script will use historical data to analyze and improve the Fleet Utilization Rate based on various factors such as operational hours, downtime, and fleet management practices. By identifying key factors, the script can provide actionable insights to optimize fleet utilization.
# Steps:
# 1. Load and preprocess the data.
# 2. Train a model to predict and analyze Fleet Utilization Rate.
# 3. Analyze the importance of different factors affecting Fleet Utilization Rate.
# 4. Provide recommendations to optimize fleet utilization.

# Data Import: Import historical data for fleet operational hours, downtime, and management practices.
# Feature Selection: Selected features that could impact Fleet Utilization Rate.
# Model Training: Trained a model to predict and analyze Fleet Utilization Rate based on these features.
# Factor Importance: Determined which factors are most important for Fleet Utilization Rate.
# Recommendations: Provided actionable recommendations based on the factor analysis.

import pandas as pd
from sklearn.linear_model import LinearRegression

# Step 1: Load and preprocess the data
def load_and_preprocess_data(file_path):
    # Load data from file
    data = pd.read_csv(file_path)
    
    # Preprocessing (example: selecting relevant columns)
    processed_data = select_features(data)
    
    return processed_data

# Step 2: Feature selection
def select_features(data):
    # Select features that could impact Fleet Utilization Rate
    # Example: Selecting relevant columns
    selected_features = data[['operational_hours', 'downtime_hours', 'fleet_management_practices']]
    return selected_features

# Step 3: Model training
def train_model(features, target):
    # Train a Linear Regression model
    model = LinearRegression()
    model.fit(features, target)
    return model

# Step 4: Analyze factor importance
def analyze_factor_importance(model, feature_names):
    # Determine factor importance from the trained model coefficients
    factor_importance = dict(zip(feature_names, model.coef_))
    sorted_importance = sorted(factor_importance.items(), key=lambda x: x[1], reverse=True)
    return sorted_importance

# Step 5: Provide recommendations
def provide_recommendations(factor_importance):
    # Provide actionable recommendations based on factor importance
    recommendations = []
    for factor, importance in factor_importance:
        recommendations.append(f"Improve {factor} to optimize fleet utilization.")
    return recommendations

# Main function to run all steps
def main():
    # Step 1: Load and preprocess the data
    file_path = 'fleet_utilization_data.csv'  # Replace with actual file path
    data = load_and_preprocess_data(file_path)
    
    # Step 2: Feature selection
    features = select_features(data)
    target = data['fleet_utilization_rate']  # Assuming 'fleet_utilization_rate' is the target variable
    
    # Step 3: Model training
    model = train_model(features, target)
    
    # Step 4: Analyze factor importance
    feature_names = features.columns
    factor_importance = analyze_factor_importance(model, feature_names)
    
    # Step 5: Provide recommendations and display them
    recommendations = provide_recommendations(factor_importance)
    
    # Display recommendations
    print("Recommendations:")
    for idx, recommendation in enumerate(recommendations, start=1):
        print(f"{idx}. {recommendation}")

if __name__ == "__main__":
    main()
