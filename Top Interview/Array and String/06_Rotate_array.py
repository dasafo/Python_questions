"""
Description

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Constraints:

    1 <= nums.length <= 105
    -231 <= nums[i] <= 231 - 1
    0 <= k <= 105

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem. Could you do it in-place with O(1) extra space?
"""

# No vamos a realizar las restrucciones ya q se hace parecido a los primero scripts realizados
class Solution:
    def rotate(self, nums:list[int], k:int) -> tuple[list[int], int]:

        k = k % len(nums)
        # si k es mayor que la longitud del array, el resto siempre coincidira con las cifras que hay desplazadas(hacer prueba con papel)

        nums[:] = nums[-k:] + nums[:-k]
        # [-k:] pilla los ultimos k elementos del array
        # [:-k] pilla los primeros elementos menos los k ultimos valores del array
        # con esto conseguimos sumar los ultimos k elementos mas el resto del principio del array original
        return nums, k


rotate = Solution().rotate

example1 = rotate([1, 2, 3, 4, 5, 6, 7], 3)
example2 = rotate([-1, -100, 3, 99], 2)

print(example1)
print(example2)

