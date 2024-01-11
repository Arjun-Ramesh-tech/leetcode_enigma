# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        result = []
        def inorder_traversal(root):
            if root is not None:
                inorder_traversal(root.left)
                result.append(root.val)
                inorder_traversal(root.right)
        inorder_traversal(root)
        mindiff = 100000
        for i in range(1,len(result)):
            mindiff = min(mindiff,result[i] - result[i-1])
        return mindiff
