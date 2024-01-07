# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        middle = 0
        link_list = head
        while(link_list):
            link_list = link_list.next
            count += 1
        if count%2 == 0:
            middle = int((count/2) + 1)
        else:
            middle = int((count+1)/2)
        print(middle)
        print(head)
        while(middle!=1):
            head = head.next
            middle = middle- 1
        return head
        
