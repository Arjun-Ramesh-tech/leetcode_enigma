# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetry_check(root1,root2):
            if root1 is None and root2 is None:
                return False
            if root1 is None or root2 is None or root1.val != root2.val:
                return True
            return symmetry_check(root1.left,root2.right) or symmetry_check(root1.right,root2.left)
        return not symmetry_check(root.left,root.right)
