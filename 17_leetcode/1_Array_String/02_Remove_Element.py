# Given an integer array nums and an integer val, remove all occurrences of
# val in nums in-place. The order of the elements may be changed. Then return
# the number of elements in nums which are not equal to val.
#
# Consider the number of elements in nums which are not equal to val be k,
# to get accepted, you need to do the following things:
#     - Change the array nums such that the first k elements of nums contain the elements
#     which are not equal to val. The remaining elements of nums are not important
#     as well as the size of nums.
#     - Return k.
# 
# Example 1:
# 
#   Input: nums = [3,2,2,3], val = 3
#   Output: 2, nums = [2,2,_,_]
#   Explanation: Your function should return k = 2, with the first two elements of nums being 2.
#   It does not matter what you leave beyond the returned k (hence they are underscores).
# 
# Example 2:
# 
#   Input: nums = [0,1,2,2,3,0,4,2], val = 2
#   Output: 5, nums = [0,1,4,0,3,_,_,_]
#   Explanation: Your function should return k = 5, with the first five elements of nums
#   containing 0, 0, 1, 3, and 4.
#   Note that the five elements can be returned in any order.
#   It does not matter what you leave beyond the returned k (hence they are underscores).
# 
# 
# Constraints:
# 
#     0 <= nums.length <= 100
#     0 <= nums[i] <= 50
#     0 <= val <= 100

def removeElement(nums, val):
    # Check constraints to ensure inputs are within the specified limits
    if not (0 <= len(nums) <= 100):
        raise ValueError("The length of nums must be between 0 and 100.")
    if not (0 <= val <= 100):
        raise ValueError("The value of val must be between 0 and 100.")
    if not all(0 <= num <= 50 for num in nums):
        raise ValueError("All elements in nums must be between 0 and 50.")
    
    # Puntero para la posición de inserción del siguiente elemento no igual a val
    k = 0

    # Recorrer todos los elementos de nums
    for i in range(len(nums)):
        if nums[i] != val:
            # Si el elemento actual no es igual a val, colocarlo en la posición k
            nums[k] = nums[i]
            k += 1  # Incrementar el puntero de inserción
    
    for i in range(k, len(nums)):
        nums[i] = '_'

    return k  # Retornar la cantidad de elementos que no son iguales a val

nums = [3, 2, 2, 3]
val = 3
k = removeElement(nums, val)
print("k:", k)  # Output: 2
print("nums after removing:", nums)  # Output: [2, 2, '_', '_']

