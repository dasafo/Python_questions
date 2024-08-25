# Given an array of integers, find the pair of adjacent elements that has
# the largest product and return that product.

#!/usr/bin/env python3
def adjacentElementProductBF(inputArray):
	largestProduct = -999999
	
	# for sanity check, assert if array contains at least 2 elements
	if len(inputArray) < 2:
		print("No pairs exists")
		return -1
    
	for i in range(0, len(inputArray)):
		for j in range(i+1, len(inputArray)):
			currentProduct = inputArray[i]*inputArray[j]
			
			if currentProduct > largestProduct:
				largestProduct = currentProduct 
	
	return largestProduct




