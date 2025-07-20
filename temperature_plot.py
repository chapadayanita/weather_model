import numpy as np
import matplotlib.pyplot as plt
from file_reader import read_temperature_data

a = -11 / 36
b = 7.5
c = -14

x = np.linspace(0, 24, 200)
temperature = a * x**2 + b * x + c

time, temp = read_temperature_data('temperature_data.csv')

plt.plot(x, temperature, label='Temperature Curve', color='blue')
plt.scatter(time, temp, color='red', label='Data Points', s=100, zorder=5)
plt.title("Simulated Temperature Curve with Data Points")
plt.xlabel("Time (Hours)")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()

