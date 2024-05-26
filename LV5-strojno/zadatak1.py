import pandas as pd
import matplotlib.pyplot as plt

# Učitavanje podataka
data = pd.read_csv('occupancy_processed.csv')

# Prikaz prvih nekoliko redaka podataka
print(data.head())

# Ispis osnovnih informacija o skupu podataka
print(data.info())

# Ispis statističkih informacija o skupu podataka
print(data.describe())

# Prikaz dijagrama raspršenja
plt.figure(figsize=(10, 6))
for count in data['Room_Occupancy_Count'].unique():
    subset = data[data['Room_Occupancy_Count'] == count]
    plt.scatter(subset['S3_Temp'], subset['S5_CO2'], label=f'Occupancy Count {count}', alpha=0.5)

plt.xlabel('S3_Temp')
plt.ylabel('S5_CO2')
plt.legend()
plt.title('Scatter Plot of S3_Temp vs S5_CO2')
plt.show()

# Broj podatkovnih primjera
print(f'Broj podatkovnih primjera: {len(data)}')

# Razdioba podatkovnih primjera po klasama
print(data['Room_Occupancy_Count'].value_counts())
