# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        left = ListNode()
        left.next = head
        right = head
        head = left
        while(right):
            if right.val == val:
                left.next = right.next
                right.next = None
                right = left.next
            else:
                left = left.next
                right = right.next
        return head.next
