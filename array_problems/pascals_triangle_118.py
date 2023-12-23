class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[1]]
        row = 2
        while(row<=numRows):
            new_arr = []
            for i in range(1,row+1):
                if i == 1 or i == row:
                    new_arr.append(1)
                else:
                    new_arr.append(answer[row-2][i-1]+ answer[row-2][i-2])
            row = row + 1
            answer.append(new_arr)
        return answer

