# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_same(self, root, subTree):
        if root is  None and subTree is  None:
            return True
        elif root is not None and subTree is not None:
            return root.val==subTree.val and self.is_same(root.left,subTree.left) and self.is_same(root.right,subTree.right)
        else:
            return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        elif self.is_same(root,subRoot):
            return True
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
