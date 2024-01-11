class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                if i == 0 :
                    perimeter += 1
                elif grid[i-1][j]==0:
                    perimeter+=1
                if i==m-1:
                    perimeter += 1
                elif grid[i+1][j]==0:
                    perimeter+=1
                if j==0:
                    perimeter += 1
                elif grid[i][j-1]==0:
                    perimeter+=1
                if j==n-1:
                    perimeter += 1
                elif grid[i][j+1]==0:
                    perimeter+=1
        return perimeter
            
                

                

        
