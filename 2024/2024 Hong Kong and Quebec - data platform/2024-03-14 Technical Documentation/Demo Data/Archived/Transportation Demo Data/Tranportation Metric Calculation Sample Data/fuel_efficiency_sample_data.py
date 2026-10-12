import pandas as pd
import numpy as np

# Function to generate synthetic data for Fuel Efficiency metric
def generate_fuel_efficiency_data(num_samples):
    """
    Generates synthetic data for Fuel Efficiency metric based on random values.

    Parameters:
    num_samples (int): Number of samples to generate.

    Returns:
    pd.DataFrame: DataFrame containing synthetic data for Fuel Efficiency.
    """
    np.random.seed(0)  # For reproducibility
    
    # Generate random fleet numbers
    fleet_numbers = np.arange(1, num_samples + 1)
    
    # Generate random features
    vehicle_age = np.random.randint(1, 10, num_samples)  # Vehicle age in years
    maintenance_frequency = np.random.randint(1000, 5000, num_samples)  # Maintenance frequency per year
    driver_behavior = np.random.uniform(0.5, 1.0, num_samples)  # Driver behavior score (0.5-1.0 scale)
    route_complexity = np.random.randint(1, 5, num_samples)  # Route complexity (1-4 scale)
    
    # Calculate Fuel Efficiency (miles per gallon)
    fuel_efficiency = np.random.uniform(4, 12, num_samples)  # Miles per gallon
    
    # Create DataFrame with fleet number as index
    data = pd.DataFrame({
        'Fleet_Number': fleet_numbers,
        'Vehicle_Age': vehicle_age,
        'Maintenance_Frequency': maintenance_frequency,
        'Driver_Behavior': driver_behavior,
        'Route_Complexity': route_complexity,
        'Fuel_Efficiency': fuel_efficiency
    })
    
    return data

# Generate sample data
num_samples = 1000
fuel_efficiency_data = generate_fuel_efficiency_data(num_samples)

# Export to CSV file
csv_file_path = 'fuel_efficiency_sample_data.csv'
fuel_efficiency_data.to_csv(csv_file_path, index=False)

print(f"Sample data for Fuel Efficiency has been generated and saved to {csv_file_path}.")

"""
### Sample Data Description for Fuel Efficiency

1. 'Fleet_Number':
   - Description: Unique identifier for each fleet unit.
   - Data Source: Generated sequentially from 1 to num_samples.
   - Format: Integer.
   - Example: 1, 2, 3, ..., 1000.
   - Meaning: Provides a unique identifier for tracking and analysis of individual fleet units.

2. 'Vehicle_Age':
   - Description: Age of the vehicle in years.
   - Data Source: Recorded from vehicle maintenance logs or fleet management systems.
   - Format: Integer (years).
   - Example: 5 years.
   - Meaning: Indicates the age of the vehicle, which can impact fuel efficiency.

3. 'Maintenance_Frequency':
   - Description: Average number of maintenance activities performed per year.
   - Data Source: Derived from maintenance logs or service records.
   - Format: Integer.
   - Example: 3000 maintenance activities per year.
   - Meaning: Reflects the frequency of maintenance interventions, which can affect vehicle performance and fuel efficiency.

4. 'Driver_Behavior':
   - Description: Assessment of driver behavior affecting fuel efficiency.
   - Data Source: Subjective assessment or based on driver performance metrics.
   - Format: Float (0.5 - 1.0 scale).
   - Example: 0.75.
   - Meaning: Evaluates driver habits and their impact on vehicle fuel consumption.

5. 'Route_Complexity':
   - Description: Complexity level of the route traveled by the vehicle.
   - Data Source: Categorized based on route characteristics or GPS data analysis.
   - Format: Integer (1-4 scale, where 1 is least complex and 4 is most complex).
   - Example: 3.
   - Meaning: Describes the difficulty level of the route, influencing fuel consumption patterns.

6. 'Fuel_Efficiency':
   - Description: Average miles per gallon (MPG) achieved by the fleet unit.
   - Data Source: Calculated from fuel consumption logs or telematics data.
   - Format: Float (miles per gallon).
   - Example: 8.5 MPG.
   - Meaning: Measures the efficiency of fuel usage for the fleet unit.

### Client Presentation Tips:

- Clarity: Ensure descriptions are clear and concise, avoiding technical jargon that may confuse non-technical stakeholders.
  
- Relevance: Connect each metric to its impact on operational efficiency and potential cost savings, highlighting actionable insights.

- Visuals: Consider using charts or graphs to illustrate trends and comparisons over time or across different segments of the fleet.
"""

