import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load CSV file
file_path = "gas_composition.csv"
df = pd.read_csv(file_path)

# Exclude the Sun
bodies = df[df["Object"] != "Sun"]

# Defining colors for each gas
color_mapping = {
    'Carbon Dioxide': '#8884d8',
    'Nitrogen': '#83a6ed',
    'Oxygen': '#8dd1e1',
    'Argon': '#82ca9d',
    'Methane': '#a4de6c',
    'Sodium': '#d0ed57',
    'Hydrogen': '#ffc658',
    'Helium': '#ff8042',
    'Other': '#ff6361'
}

# Plotting
for idx, body in bodies.iterrows():
    body_name = body['Object']
    
    # Get gas composition data
    gas_data = body.iloc[2:].copy()  # Skip Object and Mass
    
    # Filter out zero values
    gas_data = gas_data[gas_data > 0]
    
    # Skip if no gas data
    if len(gas_data) == 0:
        print(f"No atmosphere data for {body_name}")
        continue

    plt.figure(figsize=(8, 6))
    
    # Get colors for this body's gases
    colors_for_body = [color_mapping[gas] for gas in gas_data.index]
    
    # Create the pie chart
    plt.pie(
        gas_data, 
        labels=gas_data.index, 
        autopct='%1.1f%%',
        labeldistance=1.15,
        wedgeprops={'linewidth': 1, 'edgecolor': 'white'},
        colors=colors_for_body
    )
    
    plt.title(f"{body_name}'s Atmospheric Composition")
    plt.tight_layout()
    plt.savefig(f"{body_name}_atmosphere.png")
    plt.close()
