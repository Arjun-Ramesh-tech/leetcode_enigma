class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        i, j, m, n = 0, 0, len(grid), len(grid[0])
        visited_nodes = []
        if grid[0][0]!=0 or grid[m-1][n-1]!=0:
            return -1
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        visited_nodes.append((i,j))
        grid[i][j]=1
        while(visited_nodes):
            current = visited_nodes.pop(0)
            i,j = current[0], current[1]
            if i==m-1 and j==n-1:
                return grid[m-1][n-1]
            for each_direction in directions:
                new_i = i+each_direction[0]
                new_j = j+each_direction[1]
                if 0<=new_i<m and 0<=new_j<n and grid[new_i][new_j] == 0:
                    grid[new_i][new_j]= grid[i][j]+1
                    visited_nodes.append((new_i,new_j))
        return -1
            
            
            




        

        
