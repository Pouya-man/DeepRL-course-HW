import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt
from scipy.stats import norm

n = 1000
alpha = 5

# compute the tail probability
p = 1-norm.cdf(alpha)

# sample from the importance distribution
rng = default_rng()
vals = rng.exponential(scale=1, size=n) + alpha

# compute average
def w(x):
  return 1/np.sqrt(2*np.pi)*np.exp(-x**2/2+x-alpha)

Ihat = np.cumsum(w(vals))/ np.arange(1, n+1)

# plot
plt.plot(Ihat)
plt.axhline(y=p, color="r")
