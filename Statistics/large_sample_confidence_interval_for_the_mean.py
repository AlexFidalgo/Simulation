import numpy as np
import matplotlib.pyplot as plt

# Exponential distribution
lam = 0.5  # rate parameter
scale = 1/lam  # scale parameter
pop_mean = scale # population mean
pop_std = scale # population standard deviation

# Sample size (for n > 40, we can assume a normal distribution)
n = 40

# Samples from the exponential distribution
samples = np.random.exponential(scale, (n, 10000))

# Sample mean and standard deviation
sample_mean = np.mean(samples, axis=0)
sample_std = np.std(samples, axis=0, ddof=1)

# Standardized variable z for each sample
z_scores = (sample_mean - pop_mean) / (sample_std / np.sqrt(n))

# Plot the distribution of z scores
plt.hist(z_scores, bins=30, density=True)
plt.xlim([-10, 10]) # sets the x-axis limits to be fixed
plt.xlabel('Standardized sample mean')
plt.ylabel('Probability density')
