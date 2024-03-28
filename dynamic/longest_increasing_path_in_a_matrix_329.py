class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        storage = {}
        m = len(matrix)
        n = len(matrix[0])
        def recurse_all_paths(i,j):
            left,right,top,bottom = 0,0,0,0
            left_i,right_i,top_i,bottom_i = False, False, False, False
            if (i,j) in storage.keys():
                return storage[(i,j)]
            if 0<=i+1<m and matrix[i][j]<matrix[i+1][j]:
                right_i = True
                if (i+1,j) not in storage.keys():
                    right = recurse_all_paths(i+1,j)
                else:
                    right = storage[(i+1,j)]
            if 0<=i-1<m and matrix[i][j]<matrix[i-1][j]:
                left_i = True
                if (i-1,j) not in storage.keys():
                    left = recurse_all_paths(i-1,j)
                else:
                    left = storage[(i-1,j)]
            if 0<=j-1<n and matrix[i][j]<matrix[i][j-1]:
                top_i = True
                if (i,j-1) not in storage.keys():
                    top = recurse_all_paths(i,j-1)
                else:
                    top = storage[(i,j-1)]
            if 0<=j+1<n and matrix[i][j]<matrix[i][j+1]:
                bottom_i = True
                if (i,j+1) not in storage.keys():
                    bottom = recurse_all_paths(i,j+1)
                else:
                    bottom = storage[(i,j+1)]
            if not (top_i or bottom_i or left_i or right_i):
                return 1
            storage[(i,j)] = max(top,left,right,bottom) + 1
            return storage[(i,j)]
        maxDistance = 0
        for i in range(m):
            for j in range(n):
                maxDistance = max(maxDistance,recurse_all_paths(i,j))
        return maxDistance
            
