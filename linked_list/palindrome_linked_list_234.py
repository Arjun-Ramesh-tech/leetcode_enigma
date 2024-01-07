# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.main_pointer = head
        def recursive_check(current_node):
            if current_node is None:
                return True
            else:
                if not recursive_check(current_node.next):
                    return False
                if self.main_pointer.val != current_node.val:
                    return False
                self.main_pointer =self.main_pointer.next
            return True
        return recursive_check(head)
