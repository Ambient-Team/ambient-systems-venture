import pandas as pd
import numpy as np

# Function to generate synthetic data for Fleet Utilization Rate
def generate_fleet_utilization_data(num_samples):
    """
    Generates synthetic data for Fleet Utilization Rate metric based on random values.

    Parameters:
    num_samples (int): Number of samples to generate.

    Returns:
    pd.DataFrame: DataFrame containing synthetic data for Fleet Utilization Rate.
    """
    np.random.seed(0)  # For reproducibility
    
    # Generate random fleet numbers
    fleet_numbers = np.arange(1, num_samples + 1)
    
    # Generate random features
    operational_hours = np.random.randint(80, 200, num_samples)  # Operational hours per week
    downtime_hours = np.random.randint(10, 50, num_samples)  # Downtime hours per week
    fleet_management_practices = np.random.uniform(0.7, 1.0, num_samples)  # Fleet management practices effectiveness (0.7-1.0 scale)
    
    # Calculate Fleet Utilization Rate (%)
    total_available_time = operational_hours + downtime_hours
    fleet_utilization_rate = (operational_hours / total_available_time) * 100
    
    # Create DataFrame with fleet number as index
    data = pd.DataFrame({
        'Fleet_Number': fleet_numbers,
        'Operational_Hours': operational_hours,
        'Downtime_Hours': downtime_hours,
        'Fleet_Management_Practices': fleet_management_practices,
        'Fleet_Utilization_Rate': fleet_utilization_rate
    })
    
    return data

# Generate sample data
num_samples = 1000
fleet_utilization_data = generate_fleet_utilization_data(num_samples)

# Export to CSV file
csv_file_path = 'fleet_utilization_sample_data.csv'
fleet_utilization_data.to_csv(csv_file_path, index=False)

print(f"Sample data for Fleet Utilization Rate has been generated and saved to {csv_file_path}.")

"""
### Sample Data Description for Fleet Utilization Rate

1. 'Fleet_Number':
   - Description: Unique identifier for each fleet unit.
   - Data Source: Generated sequentially from 1 to num_samples.
   - Format: Integer.
   - Example: 1, 2, 3, ..., 1000.
   - Meaning: Provides a unique identifier for tracking and analysis of individual fleet units.

2. 'Operational_Hours':
   - Description: Total hours per week that the fleet units are actively engaged in operations.
   - Data Source: Extracted from operational logs or fleet management systems.
   - Format: Integer (hours per week).
   - Example: 120 hours.
   - Meaning: Represents the actual time the fleet spends actively fulfilling tasks, excluding downtime.

3. 'Downtime_Hours':
   - Description: Total hours per week that fleet units are not in operation due to maintenance, repairs, or scheduled breaks.
   - Data Source: Recorded from downtime logs or maintenance records.
   - Format: Integer (hours per week).
   - Example: 30 hours.
   - Meaning: Reflects the non-operational periods affecting fleet availability and utilization.

4. 'Fleet_Management_Practices':
   - Description: Evaluation of management practices aimed at optimizing fleet utilization efficiency.
   - Data Source: Subjective assessment based on operational strategies and management protocols.
   - Format: Float (0.0 - 1.0 scale).
   - Example: 0.85.
   - Meaning: Indicates the effectiveness of strategies implemented to maximize fleet operational uptime.

5. 'Fleet_Utilization_Rate':
   - Description: Percentage of total available time that the fleet units are actively in use.
   - Data Source: Calculated based on 'Operational_Hours' and 'Downtime_Hours'.
   - Format: Float (%).
   - Example: 80%.
   - Calculation: Fleet Utilization Rate = (Operational Hours / Total Available Time) * 100, where Total Available Time = Operational Hours + Downtime Hours.
   - Meaning: Measures the efficiency of fleet usage and operational capacity.

### Client Presentation Tips:

- Clarity: Ensure descriptions are clear and concise, avoiding technical jargon that may confuse non-technical stakeholders.
  
- Relevance: Connect each metric to its impact on operational efficiency and potential cost savings, highlighting actionable insights.

- Visuals: Consider using charts or graphs to illustrate trends and comparisons over time or across different segments of the fleet.
"""