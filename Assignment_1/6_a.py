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

# normal density with u = 0 and s = 3
list_2 = []
for i in range(0, 10_000):
    list_2.append(3 * math.sqrt(2) * erfinv(2 * list[i] - 1))
    
plt.hist(list_2, bins=np.arange(min(list_2), max(list_2) + 0.5, 0.5))
plt.title('normal distribution from inverse cdf method')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.show()
