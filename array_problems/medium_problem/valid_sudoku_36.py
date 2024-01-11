class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checksudoku(board,i,j):
            for k in range(9):
                if k!=j and board[i][k] == board[i][j]:
                    return False
            for k in range(9):
                if k!=i and board[k][j] == board[i][j]:
                    return False
            a,b = i - (i%3), j - (j%3)
            for k in range(a,a+3):
                for h in range(b,b+3):
                    if k!=i and h !=j and board[i][j]== board[k][h]:
                        return False
            return True
        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    if checksudoku(board,i,j) ==False:
                        return False
        return True
        
