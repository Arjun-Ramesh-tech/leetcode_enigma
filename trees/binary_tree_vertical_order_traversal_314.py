# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        visited, columnTable, current_index = [(root,0)], defaultdict(list), 0
        while(visited):
            node, index = visited.pop(0)
            columnTable[index].append(node.val)
            if node.left is not None:
                visited.append((node.left,index-1))
            if node.right is not None:
                visited.append((node.right,index+1))
        return [columnTable[i] for i in sorted(columnTable.keys())]
