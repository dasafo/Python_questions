"""
Description

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:

    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

class Solution:
    def majorityElement(self, nums:list[int]) -> int:
        if not (1<= len(nums)<=5*10**4):
            raise ValueError("La longitud del array esta fuera del intervalo [1, 5*10^4]")

        for num in nums:
            if not (-109 <= num <= 109):
                raise ValueError(f"El valor {num} esta fuera de rango [-109, 109]")

        count = 0
        candidate = None

        for num in nums:
            if count ==0:
                candidate = num
            count += 1 if num ==candidate else -1

        return candidate

majorityElement = Solution().majorityElement

example1 = [3, 2, 3]
example2 = [2, 2, 1, 1, 1, 2, 2]

output1 = majorityElement(example1)
output2 = majorityElement(example2)

print(output1)
print(output2)

