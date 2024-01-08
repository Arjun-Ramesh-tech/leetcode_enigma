# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def checkTree(p,q):
            if p is None and q is None:
                return False
            if (p is None and q is not None) or (p is not None and q is None):
                return True
            if (p.val== q.val):
                return checkTree(p.left,q.left) or checkTree(p.right,q.right)
            return True
        return not checkTree(p,q)
        
