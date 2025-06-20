import numpy as np

# Monthly temperature data (°C) for a year
temps = np.array([30.5, 32.0, 35.1, 38.3, 40.0, 39.5, 36.8, 34.2, 33.0, 31.5, 29.0, 28.2])

print("Monthly Temperatures:", temps)

# 1. Basic Statistics
print("Max Temperature:", np.max(temps))
print("Min Temperature:", np.min(temps))
print("Average Temperature:", np.mean(temps))
print("Median Temperature:", np.median(temps))
print("Standard Deviation:", np.std(temps))

# 2. Find months with temperature > 35°C
hot_months = np.where(temps > 35)
print("Hot Months Indexes (Temp > 35°C):", hot_months[0])
print("Temperatures in Hot Months:", temps[hot_months])

# 3. Normalize the temperature data (0 to 1 scale)
temp_min = np.min(temps)
temp_max = np.max(temps)
normalized = (temps - temp_min) / (temp_max - temp_min)
print("Normalized Temperatures:", np.round(normalized, 2))

# 4. Sort temperatures
sorted_temps = np.sort(temps)
print("Sorted Temperatures:", sorted_temps)
