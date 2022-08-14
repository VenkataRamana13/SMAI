from matplotlib import pyplot as plt
import math
import numpy as np
import random
from scipy.special import erfinv

# generating 10,000 random numbers between 0 and 1
def random_numbers():
    list = []
    for i in range(0, 10_000):
        n = random.random()
        list.append(n)
    return list
list = random_numbers()

# rayleigh density with s = 1
list_3 = []
for i in range(0, 10_000):
    list_3.append(math.sqrt(2 * math.log(1/(1-list[i]))))

plt.hist(list_3, bins=np.arange(min(list_3), max(list_3) + 0.1, 0.1))
plt.title('Rayleigh distribution plotted using inverse cdf method')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.show()
