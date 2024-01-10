class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m = len(mat)
        diagonal_sum = -mat[m//2][m//2] if m%2!=0 else 0
        for i in range(m):
            diagonal_sum += mat[i][i] + mat[i][m-i-1]
        return diagonal_sum
