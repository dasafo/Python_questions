#  Following is the provided numPy array. Return array of items
#  by taking the third column from all rows

# sampleArray = numpy.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])

import numpy as np

arr1 = np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])

arr2 = arr1[...,2]
print(arr2)
