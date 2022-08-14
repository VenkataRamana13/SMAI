from matplotlib import pyplot as plt
import numpy as np
import random
def random_numbers():
    sum = 0
    for i in range(0, 500):
        n = random.random()
        sum += n
    return sum    
list = []
for i in range(0, 50_000):
    list.append(random_numbers())
plt.hist(list, bins=np.arange(min(list), max(list) +  1, 1))
plt.show()

