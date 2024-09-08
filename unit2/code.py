import numpy as np
import matplotlib.pyplot as plt

# samples
n_samples = 10000

# Generate sample
normal_sample_means = np.cumsum(np.random.normal(0, 1, n_samples)) / np.arange(1, n_samples + 1)
cauchy_sample_means = np.cumsum(np.random.standard_cauchy(n_samples)) / np.arange(1, n_samples + 1)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(np.arange(1, n_samples + 1), normal_sample_means, label='Normal Distribution')
plt.plot(np.arange(1, n_samples + 1), cauchy_sample_means, label='Cauchy Distribution')
plt.xscale('log')  # Log scale for better visualization
plt.xlabel('Number of Samples (log scale)')
plt.ylabel('Sample Mean')
plt.title('Comparison of Sample Means: Normal vs Cauchy Distribution')
plt.legend()
plt.show()
