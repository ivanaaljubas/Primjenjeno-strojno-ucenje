import numpy as np
import matplotlib.pyplot as plt

# a) Učitavanje datoteke mtcars.csv
data = np.loadtxt(open("C:\\Users\\Ivana\\Desktop\\LV2-strojno\\mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)

# b) Prikažite ovisnost potrošnje automobila (mpg) o konjskim snagama (hp)
plt.scatter(data[:, 1], data[:, 0], label='mpg vs. hp')

# c) Na istom grafu prikažite i informaciju o težini pojedinog vozila
# Veličina točkice neka bude u skladu sa težinom (wt)
plt.scatter(data[:, 1], data[:, 0], s=data[:, 5]*10, alpha=0.5, label='mpg vs. hp & wt')

plt.xlabel('Konjske snage (hp)')
plt.ylabel('Potrošnja goriva (mpg)')
plt.title('Ovisnost potrošnje automobila o konjskim snagama')
plt.legend()
plt.grid(True)
plt.show()

# d) Izračun minimalne, maksimalne i srednje vrijednosti potrošnje (mpg) automobila
mpg_values = data[:, 0]
min_mpg = np.min(mpg_values)
max_mpg = np.max(mpg_values)
mean_mpg = np.mean(mpg_values)
print("Minimalna potrošnja (mpg):", min_mpg)
print("Maksimalna potrošnja (mpg):", max_mpg)
print("Srednja potrošnja (mpg):", mean_mpg)

# e) Ponovite zadatak pod d), ali samo za automobile sa 6 cilindara (cyl)
cyl_6_data = data[data[:, 3] == 6]  # Filter podataka za automobile sa 6 cilindara
mpg_values_cyl_6 = cyl_6_data[:, 0]
min_mpg_cyl_6 = np.min(mpg_values_cyl_6)
max_mpg_cyl_6 = np.max(mpg_values_cyl_6)
mean_mpg_cyl_6 = np.mean(mpg_values_cyl_6)
print("\nZa automobile sa 6 cilindara:")
print("Minimalna potrošnja (mpg):", min_mpg_cyl_6)
print("Maksimalna potrošnja (mpg):", max_mpg_cyl_6)
print("Srednja potrošnja (mpg):", mean_mpg_cyl_6)
