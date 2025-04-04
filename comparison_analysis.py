import matplotlib.pyplot as plt
import pandas as pd

# Load CSV file
file_path = "planets.csv"
data = pd.read_csv(file_path)

# Scatter plot: Diameter vs. Gravity
plt.figure(figsize=(10, 6))
plt.scatter(data['diameter'], data['gravity'], color='orange', edgecolors='black')
for i, planet in enumerate(data['planet']):
    plt.text(data['diameter'][i], data['gravity'][i], planet, fontsize=9, ha='right', va='bottom')
plt.xlabel('Diameter (km)')
plt.ylabel('Gravity (m/s²)')
plt.title('Diameter vs. Gravity of Planets')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Bar Chart - Number of Moons
plt.figure(figsize=(10, 6))
moon_counts = data[data['number_of_moons'] != 'Unknown*']
bars = plt.bar(moon_counts['planet'], moon_counts['number_of_moons'])
plt.xlabel('Planet')
plt.ylabel('Number of Moons')
plt.title('Number of Moons in the Solar System')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Scatter plot - Mean Temperature vs. Distance from Sun
plt.figure(figsize=(10, 6))
plt.scatter(data['distance_from_sun'], data['mean_temperature'], color='skyblue', edgecolors='black')
for i, planet in enumerate(data['planet']):
    plt.text(data['distance_from_sun'][i], data['mean_temperature'][i], planet, fontsize=9, ha='right', va='bottom')
plt.xlabel('Distance from Sun (AU)')
plt.ylabel('Mean Temperature (°C)')
plt.title('Mean Temperature vs. Distance from Sun')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Bar Chart - Comparison of Length of Days wrt Earth
# Extract planet names and length_of_day values
planet_names = data['planet'].tolist()
day_lengths_hours = data['length_of_day'].tolist()
day_lengths_earth_days = [hours / 24 for hours in day_lengths_hours]

# Color palette for the planets
planet_colors = {
    'Mercury': '#A9A9A9',  # Gray
    'Venus': '#FFD700',    # Gold
    'Earth': '#1E90FF',    # Blue
    'Mars': '#FF4500',     # Red-orange
    'Jupiter': '#CD853F',  # Peru/brown
    'Saturn': '#DAA520',   # Goldenrod
    'Uranus': '#ADD8E6',   # Light blue
    'Neptune': '#4169E1',  # Royal blue
    'Pluto': '#8B008B'     # Dark magenta
}

# Plotting
plt.figure(figsize=(12, 6))
all_bars = plt.bar(planet_names, day_lengths_earth_days, 
                  color=[planet_colors.get(p, '#000000') for p in planet_names])
plt.xlabel('Planet')
plt.ylabel('Length of Day (Earth Days)')
plt.title('Planetary Day Lengths Compared to Earth')
plt.yscale('log')  # Using log scale due to huge differences
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add value labels
for bar in all_bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
            f'{height:.2f}',
            ha='center', va='bottom', rotation=0)

plt.tight_layout()
plt.savefig('all_objects_day_lengths.png', dpi=300)
plt.show()
