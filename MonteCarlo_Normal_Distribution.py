# Plot a normal distribution with mean 1000 and standard deviation 100 by sampling via simulation

import random
import math
import matplotlib.pyplot as plt
import numpy as np

# Number of light bulbs to simulate
n = 100000

# Mean and standard deviation of lifespan
mean = 1000
std_dev = 100

# Simulate the lifespan of n light bulbs
lifespans = [random.normalvariate(mean, std_dev) for i in range(n)]

# Estimate the average lifespan of the light bulbs
avg_lifespan = sum(lifespans) / n

# Estimate the standard error of the mean
std_error = std_dev / math.sqrt(n)

# Calculate the 95% confidence interval for the estimate
lower_bound = avg_lifespan - 1.96 * std_error
upper_bound = avg_lifespan + 1.96 * std_error

print("Estimated average lifespan: {:.2f}".format(avg_lifespan))
print("95% confidence interval: ({:.2f}, {:.2f})".format(lower_bound, upper_bound))

# Generate x values from -3 to 3 standard deviations from the mean
x = np.linspace(mean - 3*std_dev, mean + 3*std_dev, 1000)

# Calculate the corresponding y values from the normal distribution
y = 1/(std_dev * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mean)/std_dev)**2)

# Plot the normal distribution
plt.plot(x, y)
plt.xlabel('Lifespan')
plt.ylabel('Probability density')
plt.title('Normal distribution with mean {} and standard deviation {}'.format(mean, std_dev))
plt.show()
