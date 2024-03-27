class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(1,m):
            for j in range(1,n):
                if i-1>=0 and j-1>=0 and matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True        
