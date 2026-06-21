import random
import matplotlib.pyplot as plt

numbers_a = list(range(1, 13))
numbers_b = random.sample(range(1, 1000), 12)

plt.plot(numbers_a, numbers_b)
plt.show()



