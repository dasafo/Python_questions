# Given an array of integers nums and an integer target, return indices of
# the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you 
# may not use the same element twice.
# You can return the answer in any order.
# 
# 
# Example 1:
# 
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# 
# Example 2:
# 
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# 
# Example 3:
# 
# Input: nums = [3,3], target = 6
# Output: [0,1]
# 
# 
# Constraints:
# 
#     2 <= nums.length <= 104
#     -109 <= nums[i] <= 109
#     -109 <= target <= 109
#     Only one valid answer exists.


def twoSum(nums, target):
    # Validación de la longitud del array
    if not (2 <= len(nums) <= 104):
        raise ValueError("La longitud de nums debe estar entre 2 y 104.")

    # Validación del rango de los elementos en nums
    if any(num < -109 or num > 109 for num in nums):
        raise ValueError("Todos los elementos de nums deben estar en el rango de -109 a 109.")

    # Validación del rango del target
    if target < -109 or target > 109:
        raise ValueError("El target debe estar en el rango de -109 a 109.")
    
    # Diccionario para almacenar el índice de los elementos
    num_to_index = {}
    
    # Recorrer la lista
    for i, num in enumerate(nums):
        # Calcular el complemento
        complement = target - num
        
        # Verificar si el complemento ya está en el diccionario
        if complement in num_to_index:
            return [num_to_index[complement], i]
        
        # Almacenar el índice del número actual en el diccionario
        num_to_index[num] = i

# Ejemplo de uso con validaciones
try:
    print(twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
    print(twoSum([3, 2, 4], 6))       # Output: [1, 2]
    print(twoSum([3, 3], 6))          # Output: [0, 1]
    print(twoSum([10**10, 2, 4], 6))  # Esto lanzará un ValueError
except ValueError as e:
    print(e)


