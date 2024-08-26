# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# - Example 1:
#       Input: l1 = [2,4,3], l2 = [5,6,4]
#       Output: [7,0,8]
#       Explanation: 342 + 465 = 807.
# 
# - Example 2:
#       Input: l1 = [0], l2 = [0]
#       Output: [0]
# 
# - Example 3:
#       Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
#       Output: [8,9,9,9,0,0,0,1]
# 
# - Constraints:
#     The number of nodes in each linked list is in the range [1, 100].
#     0 <= Node.val <= 9
#     It is guaranteed that the list represents a number that does not have leading zeros.

# Definition for singly-linked list.
# A node here is a number in a list that points to another node via next.
# Example 2

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # Store the value of the node
        self.next = next  # Reference to the next node in the list

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialize a dummy node to act as the head of the result linked list
        dummy = ListNode(0)
        current = dummy  # Pointer to build the result list
        carry = 0  # Initialize the carry to 0

        # Loop until both l1 and l2 are exhausted and there is no carry left
        while l1 or l2 or carry:
            # Get values from the current nodes, or 0 if the list has ended
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Compute the sum of values plus carry
            val = v1 + v2 + carry
            carry = val // 10  # Calculate the new carry for the next digit
            val = val % 10  # Get the digit to store in the current node

            # Create a new node with the computed value and attach it to the result list
            current.next = ListNode(val)
            current = current.next  # Move to the next position in the result list

            # Move to the next nodes in l1 and l2, if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the result list, which starts after the dummy node
        return dummy.next

# Helper function to create a linked list from a list of values
def create_linked_list(lst):
    dummy = ListNode(0)  # Dummy node to simplify list construction
    current = dummy  # Pointer to the last node in the constructed list
    for val in lst:
        current.next = ListNode(val)  # Create a new node and link it
        current = current.next  # Move the pointer to the new last node
    return dummy.next  # Return the list, skipping the dummy node

# Helper function to convert a linked list back into a Python list
def linked_list_to_list(head):
    result = []  # List to store the values from the linked list
    while head:
        result.append(head.val)  # Append the current node's value to the result list
        head = head.next  # Move to the next node
    return result  # Return the constructed list

# Test the solution with an example
solution = Solution()

# Example 1
l1 = create_linked_list([2, 4, 3])  # Create linked list representing number 342
l2 = create_linked_list([5, 6, 4])  # Create linked list representing number 465
result = solution.addTwoNumbers(l1, l2)  # Sum the two numbers represented by linked lists
print("Example 1:", linked_list_to_list(result))  # Output the result as a list


# Example 2
l1 = create_linked_list([0])
l2 = create_linked_list([0])
result = solution.addTwoNumbers(l1, l2)
print("Example 2:", linked_list_to_list(result))

# Example 3
l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = create_linked_list([9, 9, 9, 9])
result = solution.addTwoNumbers(l1, l2)
print("Example 3:", linked_list_to_list(result))
