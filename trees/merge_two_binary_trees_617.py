# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        elif root1 is None and root2 is not None:
            node = TreeNode(root2.val)
            node.left = self.mergeTrees(root1,root2.left)
            node.right = self.mergeTrees(root1,root2.right)
        elif root2 is None and root1 is not None:
            node = TreeNode(root1.val)
            node.left = self.mergeTrees(root1.left,root2)
            node.right = self.mergeTrees(root1.right,root2)
        else:
            node = TreeNode(root1.val+root2.val)
            node.left = self.mergeTrees(root1.left,root2.left)
            node.right = self.mergeTrees(root1.right,root2.right)
        return node
