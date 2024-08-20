# Split the array into four equal-sized sub-arrays

# Note: Create an 8X3 integer array from a range between 10 to 34
# such that the difference between each element is 1 and then
# Split the array into four equal-sized sub-arrays.

import numpy

print("Creating 8X3 array using numpy.arange")
sampleArray = numpy.arange(10, 34, 1)
sampleArray = sampleArray.reshape(8,3)
print (sampleArray)

print("\nDividing 8X3 array into 4 sub array\n")
subArrays = numpy.split(sampleArray, 4) 
print(subArrays)
