import numpy as np
tempretures = np.array([32.5, 31.8, 33.0, 35.2, 36.6])
samples = np.random.choice(tempretures, size=100000, replace=True)
average = np.mean(samples)
print(average)
