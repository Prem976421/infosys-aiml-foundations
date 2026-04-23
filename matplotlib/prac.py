import matplotlib.pyplot as plt
import numpy as np

# 1. Generate the data (corrected x1 to x)
x = np.arange(0.0, 5.0, 0.1)
y = np.cos(2 * np.pi * x) * np.exp(-x)

fig = plt.figure()
ax = fig.add_axes([0.15,0.15,0.75,0.75])
ax.plot(x, y, color = "black", marker = "o", linestyle = "-", markerfacecolor = "#62eec780", markeredgecolor = "#beeddf")
ax.set_title('Damped Oscillation')
ax.set_xlabel('voltage (mv)',color = 'green')
ax.set_ylabel('time (s)', color = 'green')
plt.show()