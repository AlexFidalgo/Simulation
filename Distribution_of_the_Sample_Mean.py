import numpy as np
import matplotlib.pyplot as plt

n = 100000 #sample size
k = 5000 #number of samples

# Generate k samples of n observations from a normal distribution
samples = np.random.normal(loc=0, scale=1, size=(k, n))

# Calculate the sample means
sample_means = np.mean(samples, axis=1)

# Calculate the expected value of the sample means and the standard error of the sample mean
expected_value = np.mean(sample_means)
standard_error = np.std(sample_means, ddof=1)

# Print the expected value and standard error
print(f"Expected value of sample means: {expected_value:.5f}")
print("True expected value: 0")
print()
print(f"Standard error of sample mean: {standard_error:.5f}")
print(f"True standard error: {1/(n**0.5)}")

# Plot the distribution of the sample means
plt.hist(sample_means, bins= 1000)
plt.xlabel('Sample mean')
plt.ylabel('Frequency')
plt.title(f'Distribution of Sample Means (n={n})')
plt.xlim(-0.03, 0.03)
plt.show()

# higher n means lower standard error
