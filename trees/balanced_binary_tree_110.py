# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.flag = True
        def checkBalance(root):
            if root is None:
                return 0
            left = checkBalance(root.left)
            right = checkBalance(root.right)
            if abs(left- right)>1:
                self.flag = False
            return max(left,right) + 1
        checkBalance(root)
        return self.flag
        
