# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        unique_elements = []
        left = ListNode()
        right = head
        left.next = head
        head = left
        while(right):
            if right.val in unique_elements:
                left.next = right.next
                right.next = None
                right = left.next
            else:
                unique_elements.append(right.val)
                left = left.next
                right = right.next
        return head.next
                
        
