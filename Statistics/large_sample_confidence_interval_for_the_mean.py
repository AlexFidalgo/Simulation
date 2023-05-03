import numpy as np
import matplotlib.pyplot as plt

# Set the parameters of the exponential distribution
lam = 0.5  # rate parameter
scale = 1/lam  # scale parameter

# Set the sample size
n = 100

# Generate samples from the exponential distribution
samples = np.random.exponential(scale, (n, 10000))

# Calculate the sample mean and standard deviation
sample_mean = np.mean(samples, axis=0)
sample_std = np.std(samples, axis=0, ddof=1)

# Calculate the population mean and standard deviation
pop_mean = scale
pop_std = scale

# Calculate the standardized variable z for each sample
z_scores = (sample_mean - pop_mean) / (sample_std / np.sqrt(n))

# Plot the distribution of z scores
plt.hist(z_scores, bins=30, density=True)
plt.xlabel('Standardized sample mean')
plt.ylabel('Probability density')
