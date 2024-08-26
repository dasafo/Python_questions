# Given an integer array nums sorted in non-decreasing order, remove the
# duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same. Then return
# the number of unique elements in nums.
# 
# Consider the number of unique elements of nums to be k, to get accepted,
# you need to do the following things:
# 
#     - Change the array nums such that the first k elements of nums contain
#     the unique elements in the order they were present in nums initially.
#     The remaining elements of nums are not important as well as the size of nums.
#     - Return k.
#
# Example 1:
#   Input: nums = [1,1,2]
#   Output: 2, nums = [1,2,_]
#   Explanation: Your function should return k = 2, with the first two elements
#   of nums being 1 and 2 respectively.
#   It does not matter what you leave beyond the returned k (hence they are underscores).
# 
# Example 2:
#   Input: nums = [0,0,1,1,1,2,2,3,3,4]
#   Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
#   Explanation: Your function should return k = 5, with the first five elements
#   of nums being 0, 1, 2, 3, and 4 respectively.
#   It does not matter what you leave beyond the returned k (hence they are underscores).
# 
# 
# Constraints:
# 
#     1 <= nums.length <= 3 * 104
#     -100 <= nums[i] <= 100
#     nums is sorted in non-decreasing order.

def removeDuplicates(nums):
    if not nums:
        return 0  # Return 0 if nums is empty

    # Start with the first unique element
    k = 1

    # Traverse the sorted array starting from the second element
    for i in range(1, len(nums)):
        if nums[i] != nums[k - 1]:  # Check if the current element is different from the last unique element
            nums[k] = nums[i]  # Place the unique element at index k
            k += 1  # Increment the count of unique elements

    # Optional: Set elements beyond the first k elements to None or some placeholder
    for i in range(k, len(nums)):
        nums[i] = '_'

    return k  # Return the number of unique elements

nums = [1, 1, 2]
k = removeDuplicates(nums)
print("k:", k)  # Output: 2
print("nums after removing duplicates:", nums)  # Output: [1, 2, '_']

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = removeDuplicates(nums)
print("k:", k)  # Output: 5
print("nums after removing duplicates:", nums)  # Output: [0, 1, 2, 3, 4, '_', '_', '_', '_', '_']

