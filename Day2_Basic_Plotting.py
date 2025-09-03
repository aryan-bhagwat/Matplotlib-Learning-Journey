# Day 2 – Basic Plotting

import matplotlib.pyplot as plt


# Data
x = [1, 2, 3, 4, 5]
y1 = [i**2 for i in x]   # squares
y2 = [i**3 for i in x]   # cubes

# Plot squares
plt.plot(x, y1, label="Squares")

# Plot cubes
plt.plot(x, y2, label="Cubes")

# Labels
plt.xlabel("X values")
plt.ylabel("Y values")

# Title
plt.title("Squares and Cubes")

# Grid
plt.grid(True)

# Legend
plt.legend()

# Show plot
plt.show()
