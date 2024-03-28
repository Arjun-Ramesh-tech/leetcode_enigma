class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cols = []
        rows = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows.append(i)
        for i in range(n):
            for j in range(m):
                if grid[j][i] == 1:
                    cols.append(i)
        middle_column = cols[int(len(cols)/2)]
        middle_row = rows[int(len(rows)/2)]
        distance = 0
        for i in rows:
            distance += abs(i-middle_row)
        for i in cols:
            distance += abs(i-middle_column)
        return distance

        
