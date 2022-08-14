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

# exponential density with lambda = 1.5
list_4 = []
for i in range(0, 10_000):
    list_4.append(2 / 3 * math.log(1/(1 - list[i])))

plt.hist(list_4, bins=np.arange(min(list_4), max(list_4) + 0.1, 0.1))
plt.title('Exponential distribution using inverse cdf method')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.show()
