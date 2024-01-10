# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return None
        else:
            answer = str(root.val)
            left = self.tree2str(root.left)
            right = self.tree2str(root.right)
            if left is not None:
                answer += "(" + left + ")"
            if left is None and right is not None:
                answer += "()"
            if right is not None:
                answer += "(" + right + ")"
            return  answer
        
