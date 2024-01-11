# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        small = head
        large = head.next
        while(small is not None and large is not None and large.next is not None):
            if small == large:
                return True
            small = small.next
            large = large.next.next
        return False

        
        
        
