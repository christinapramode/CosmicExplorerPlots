import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.image as mpimg

# Load CSV file
file_path = "planets.csv"
df = pd.read_csv(file_path)

# Select fields
planets = df['planet']
obliquities = df['obliquity_to_orbit']

# Dictionary linking planets to image files
planet_images = {
    'Mercury': 'mercury.jpeg',
    'Venus': 'venus.jpeg',
    'Earth': 'earth.jpeg',
    'Mars': 'mars.jpeg',
    'Jupiter': 'jupiter.jpeg',
    'Saturn': 'saturn.jpeg',
    'Uranus': 'uranus.jpeg',
    'Neptune': 'neptune.jpeg',
    'Pluto': 'pluto.jpeg'
}

# Function to visualize axial tilt with planet image
def plot_axial_tilt(planet, obliquity):
    fig, ax = plt.subplots(figsize=(4, 6))
    
    # Load and display image
    img_file = planet_images.get(planet, None)
    img = mpimg.imread(img_file)
    ax.imshow(img, extent=[-1, 1, -1, 1], aspect='auto')
    
    # Draw tilt line
    angle = np.deg2rad(obliquity)
    x_vals = np.array([-1, 1]) * np.cos(angle)
    y_vals = np.array([-1, 1]) * np.sin(angle)
    ax.plot(x_vals, y_vals, 'r-', linewidth=2, label=f'Tilt: {obliquity}\u00b0')
    
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.set_xticks([-1, 0, 1])
    ax.set_yticks([-1, 0, 1])
    ax.legend()
    plt.title(f'{planet} Axial Tilt')
    plt.show()

# Plotting
for planet, obliquity in zip(planets, obliquities):
    plot_axial_tilt(planet, obliquity)
