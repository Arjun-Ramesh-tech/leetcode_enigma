class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        index = 2
        index_values = {}
        def get_the_islands(i,j,k):
            if 0<=i<n and 0<=j<n and grid[i][j] == 1:
                grid[i][j] = index
                k += 1
                for each_direction in [(-1,0),(1,0),(0,-1),(0,1)]:
                     k = get_the_islands(i+each_direction[0],j+each_direction[1],k) 
            return k
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    index_values[index] = get_the_islands(i,j,0)
                    index +=1
        answers = set()
        previous_best = 0
        has_zero = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    has_zero = True
                    sum_value = 0
                    answers.clear()
                    for each_direction in [(-1,0),(1,0),(0,-1),(0,1)]:
                        if 0<=i+each_direction[0]<n and 0<=j+each_direction[1]<n and grid[i+each_direction[0]][j+each_direction[1]]>1:
                            answers.add(grid[i+each_direction[0]][j+each_direction[1]])
                    for each in answers:
                        sum_value += index_values[each]
                    previous_best = max(sum_value+1,previous_best)
        return previous_best if has_zero else n*n
