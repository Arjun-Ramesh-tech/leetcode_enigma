class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(grid), len(grid[0])
        while(k>0):
            grid_result = [[0]*n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i==m-1 and j == n-1:
                        grid_result[0][0] = grid[m-1][n-1]
                    elif j == n-1:
                        grid_result[i+1][0] = grid[i][j]
                    else:
                        grid_result[i][j+1] = grid[i][j]
            k -= 1
            grid = grid_result
        return grid
        
