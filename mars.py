import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "REMS_Mars_Dataset.csv"
df = pd.read_csv(file_path)

# Clean the data
def clean_numeric(column_name):
    df[column_name] = pd.to_numeric(df[column_name], errors='coerce')

numeric_columns = ["max_ground_temp(°C)", "min_ground_temp(°C)", "max_air_temp(°C)", "min_air_temp(°C)", "mean_pressure(Pa)"]
for col in numeric_columns:
    clean_numeric(col)

df.dropna(inplace=True)  # Remove rows with missing values
df['earth_date_time'] = pd.to_datetime(df['earth_date_time'].str.split(',').str[1].str.strip(), format="%Y-%m-%d %Z")
df['earth_date_time'] = df['earth_date_time'].dt.date
df.sort_values(by='earth_date_time', inplace=True)


# Line plot - Temperature Trends
plt.figure(figsize=(12, 6))
plt.plot(df['earth_date_time'], df['max_air_temp(°C)'], label='Max Air Temp (°C)', color='red')
plt.plot(df['earth_date_time'], df['min_air_temp(°C)'], label='Min Air Temp (°C)', color='blue')
plt.xlabel("Earth Date")
plt.ylabel("Temperature (°C)")
plt.title("Mars Air Temperature Trends")
plt.legend()
plt.xticks(rotation=45)
plt.show()

# Pie Chart - UV Radiation Levels
plt.figure(figsize=(6, 6))
df['UV_Radiation'].value_counts().plot.pie(autopct='%1.1f%%', wedgeprops={'linewidth': 1, 'edgecolor': 'white'}, colors=["gold", "lightblue", "lightgreen", "lightpink"])
plt.title("Distribution of UV Radiation Levels on Mars")
plt.ylabel("")
plt.show()
