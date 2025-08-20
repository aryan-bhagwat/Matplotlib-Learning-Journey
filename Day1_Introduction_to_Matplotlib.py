# Day 1 – Introduction to Matplotlib

import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a simple line plot
plt.plot(x, y)    

# show the graph
plt.show()

## Practice Set:
x = [0, 1, 2, 3, 4, 5]
y = [i**2 for i in x]

# Plot the graph using plt.plot()
plt.plot(x, y)
plt.show()