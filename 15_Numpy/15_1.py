# Create a 4X2 integer array and Prints its attributes

# Note: The element must be a type of unsigned int16. And print the following Attributes: –
# 
#     The shape of an array.
#     Array dimensions.
#     The Length of each element of the array in bytes.

import numpy as np

arr1 = np.empty([4,2], dtype=np.uint16)
print(arr1, end="\n")

print("1- Array Shape: ", arr1.shape)
print("2- Array dimensions: ", arr1.ndim)
print("3- Lenght of each element of the array in bytes: ", arr1.itemsize)


