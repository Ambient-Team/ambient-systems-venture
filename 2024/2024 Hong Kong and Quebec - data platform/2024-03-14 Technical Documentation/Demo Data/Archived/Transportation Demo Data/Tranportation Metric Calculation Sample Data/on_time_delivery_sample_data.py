import pandas as pd
import numpy as np

# Function to generate synthetic data for On-Time Delivery Rate metric
def generate_on_time_delivery_data(num_samples):
    """
    Generates synthetic data for On-Time Delivery Rate metric based on random values.

    Parameters:
    num_samples (int): Number of samples to generate.

    Returns:
    pd.DataFrame: DataFrame containing synthetic data for On-Time Delivery Rate.
    """
    np.random.seed(0)  # For reproducibility
    
    # Generate random fleet numbers
    fleet_numbers = np.arange(1, num_samples + 1)
    
    # Generate random features
    total_deliveries = np.random.randint(50, 200, num_samples)  # Total deliveries made
    on_time_deliveries = np.random.randint(40, total_deliveries + 1, num_samples)  # On-time deliveries
    
    # Calculate On-Time Delivery Rate (%)
    on_time_delivery_rate = (on_time_deliveries / total_deliveries) * 100
    
    # Create DataFrame with fleet number as index
    data = pd.DataFrame({
        'Fleet_Number': fleet_numbers,
        'Total_Deliveries': total_deliveries,
        'On_Time_Deliveries': on_time_deliveries,
        'On_Time_Delivery_Rate': on_time_delivery_rate
    })
    
    return data

# Generate sample data
num_samples = 1000
on_time_delivery_data = generate_on_time_delivery_data(num_samples)

# Export to CSV file
csv_file_path = 'on_time_delivery_sample_data.csv'
on_time_delivery_data.to_csv(csv_file_path, index=False)

print(f"Sample data for On-Time Delivery Rate has been generated and saved to {csv_file_path}.")

"""
### Sample Data Description for On-Time Delivery Rate

1. 'Fleet_Number':
   - Description: Unique identifier for each fleet unit.
   - Data Source: Generated sequentially from 1 to num_samples.
   - Format: Integer.
   - Example: 1, 2, 3, ..., 1000.
   - Meaning: Provides a unique identifier for tracking and analysis of individual fleet units.

2. 'Total_Deliveries':
   - Description: Total number of deliveries made by the fleet unit.
   - Data Source: Recorded from delivery logs or tracking systems.
   - Format: Integer.
   - Example: 150 deliveries.
   - Meaning: Represents the overall volume of deliveries completed by the fleet unit.

3. 'On_Time_Deliveries':
   - Description: Number of deliveries made on or before the scheduled delivery time.
   - Data Source: Recorded from delivery logs or tracking systems.
   - Format: Integer.
   - Example: 120 on-time deliveries.
   - Meaning: Indicates the number of deliveries that met or exceeded the scheduled delivery time.

4. 'On_Time_Delivery_Rate':
   - Description: Percentage of deliveries made on or before the scheduled delivery time.
   - Data Source: Calculated based on 'On_Time_Deliveries' and 'Total_Deliveries'.
   - Format: Float (%).
   - Example: 80%.
   - Calculation: On-Time Delivery Rate = (On-Time Deliveries / Total Deliveries) * 100.
   - Meaning: Measures the efficiency of delivery operations in meeting scheduled commitments.

### Client Presentation Tips:

- Clarity: Ensure descriptions are clear and concise, avoiding technical jargon that may confuse non-technical stakeholders.
  
- Relevance: Connect each metric to its impact on customer satisfaction and operational efficiency, highlighting actionable insights.

- Visuals: Consider using charts or graphs to illustrate trends and comparisons over time or across different segments of the fleet.
"""

