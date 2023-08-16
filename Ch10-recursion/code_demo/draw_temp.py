import matplotlib.pyplot as plt

with open('ocean_temp.csv') as temp_file:
    temps = []
    for t in temp_file:
        temps.append(float(t))

# one year for each temperature
years = range(1850, 2012)
plt.plot(years, temps)

pirate_years = range(1850, 2025, 25)
num_pirates_thousands = [20, 17, 15, 5, 0.4, 0.05, 0.025]
plt.plot(pirate_years, num_pirates_thousands, 'g2')

plt.show()
