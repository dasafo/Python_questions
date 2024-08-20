# Create a 5X2 integer array from a range between 100 to 200
# such that the difference between each element is 10

import numpy as np

arr1 = np.arange(100, 200, 10)
arr1 = arr1.reshape(5, 2)

print(arr1)
