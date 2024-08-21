'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result, queue = [], [root]
        while queue:
            current_length, current_iter = len(queue), []
            for _ in range(current_length):
                current_val = queue.pop(0)
                current_iter.append(current_val.val)
                if current_val.left:
                    queue.append(current_val.left)
                if current_val.right:
                    queue.append(current_val.right)
            result.append(current_iter)
        return result