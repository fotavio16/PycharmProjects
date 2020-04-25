from scipy.stats import binom
from matplotlib import pyplot as plt
import numpy as np

n = 5
p = 0.40
x = np.array(range(0, n+1))

prob = np.array([binom.pmf(k, n, p) for k in x])
print(prob)
# Set up the graph
plt.xlabel('x')
plt.ylabel('Probability')
plt.bar(x, prob)
plt.show()