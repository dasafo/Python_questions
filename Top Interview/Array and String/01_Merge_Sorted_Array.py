"""
 Question 1 - 88. Merge Sorted Array
 Description
 
 You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
 
 Merge nums1 and nums2 into a single array sorted in non-decreasing order.
 
 The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
 Example 1:
 
     Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
     Output: [1,2,2,3,5,6]
     Explanation: The arrays we are merging are [1,2,3] and [2,5,6]. The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
 
 Example 2:
 
     Input: nums1 = [1], m = 1, nums2 = [], n = 0
     Output: [1]
     Explanation: The arrays we are merging are [1] and []. The result of the merge is [1].
 
 Example 3:
 
     Input: nums1 = [0], m = 0, nums2 = [1], n = 1
     Output: [1]
     Explanation: The arrays we are merging are [] and [1]. The result of the merge is [1]. Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 
 Constraints:
 
     nums1.length == m + n
     nums2.length == n
     0 <= m, n <= 200
     1 <= m + n <= 200
     -10^9 <= nums1[i], nums2[j] <= 10^9
 
 Follow up:
 
 Can you come up with an algorithm that runs in O(m + n) time?
"""

class mergeNums:
       
    def merge(self, nums1:list[int], m:int, nums2:list[int], n:int) -> None:
    
        """
        Merge two sorted arrays into nums1 in-place.
        - nums1: list with m meaningful elements followed by n zeroes (space for nums2).
        - nums2: list with n meaningful elements.
        - m: number of actual elements in nums1
        - n: number of elements in nums2
        
        The result must be sorted and stored in nums1.
        """
    
        # i apunta al último elemento útil de nums1
        i = m - 1
        # j apunta al último elemento de nums2
        j = n - 1
        # k apunta al último espacio libre en nums1 (donde puede ir el máximo valor)
        k = m + n - 1
    
        # Empezamos a llenar nums1 desde el final para evitar sobreescribir elementos aún no procesados
        while i >= 0 and j >= 0:
            # Comparamos los elementos actuales de nums1 y nums2
            if nums1[i] > nums2[j]:
                # Si el elemento de nums1 es mayor, lo colocamos al final de nums1 (posición k)
                nums1[k] = nums1[i]
                i -= 1  # Avanzamos hacia atrás en nums1
            else:
                # Si el de nums2 es mayor o igual, lo colocamos en nums1[k]
                nums1[k] = nums2[j]
                j -= 1  # Avanzamos hacia atrás en nums2
            k -= 1  # En cualquier caso, retrocedemos una posición en nums1
    
        # Si nums2 tiene elementos restantes (y nums1 ya se ha vaciado), los copiamos
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
    
        # No es necesario copiar lo que queda en nums1 porque ya está en su sitio
    

nums1 = [1,2,3,0,0,0] 
m = 3
nums2 = [2,5,6]
n = 3

mergeNums().merge(nums1, m, nums2, n)
print(nums1)
