# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored
# inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m
# elements denote the elements that should be merged, and the last n elements are set to 0
# and should be ignored. nums2 has a length of n.
# 
# 
# Example 1:
#       Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
#       Output: [1,2,2,3,5,6]
#       Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
#       The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# 
# Example 2:
#       Input: nums1 = [1], m = 1, nums2 = [], n = 0
#       Output: [1]
#       Explanation: The arrays we are merging are [1] and [].
#       The result of the merge is [1].
# 
# Example 3:
#       Input: nums1 = [0], m = 0, nums2 = [1], n = 1
#       Output: [1]
#       Explanation: The arrays we are merging are [] and [1].
#       The result of the merge is [1].
#       Note that because m = 0, there are no elements in nums1. The 0 
#       is only there to ensure the merge result can fit in nums1.

# Constraints:
# 
#     nums1.length == m + n
#     nums2.length == n
#     0 <= m, n <= 200
#     1 <= m + n <= 200
#     -109 <= nums1[i], nums2[j] <= 109

def merge(nums1, m, nums2, n):
    # Check if the lengths of nums1 and nums2 match the provided values m and n
    if len(nums1) != m + n or len(nums2) != n:
        raise ValueError("Length of nums1 must be m + n and length of nums2 must be n.")
    
    # Check if m and n are within their specified ranges
    if not (0 <= m <= 200 and 0 <= n <= 200 and 1 <= m + n <= 200):
        raise ValueError("Values of m and n must be within the specified limits.")
    
    # Verify that all elements in nums1[:m] and nums2 are within the allowed range
    for lst in [nums1[:m], nums2]:
        if not all(-10**9 <= x <= 10**9 for x in lst):
            raise ValueError("All elements must be between -10^9 and 10^9.")
    
    # Initialize pointers for nums1 (p1), nums2 (p2), and the current position (p) in the merged array
    p1, p2, p = m - 1, n - 1, m + n - 1
    
    # Merge nums1 and nums2 starting from the end towards the beginning
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:  # If the current element in nums1 is larger
            nums1[p] = nums1[p1]   # Place it at the current position of the merged array
            p1 -= 1                # Move pointer p1 to the left
        else:
            nums1[p] = nums2[p2]   # Otherwise, place the current element of nums2 in the merged array
            p2 -= 1                # Move pointer p2 to the left
        p -= 1                    # Move the current position pointer p to the left

    # If there are remaining elements in nums2, copy them over to nums1
    while p2 >= 0:
        nums1[p] = nums2[p2]  # Copy the remaining elements of nums2 into nums1
        p2 -= 1               # Move pointer p2 to the left
        p -= 1                # Move pointer p to the left

# Example usage
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)  # Merge nums2 into nums1
print(nums1)  # Output should be: [1, 2, 2, 3, 5, 6]
