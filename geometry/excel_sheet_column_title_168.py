class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        answer = ""
        while(columnNumber > 0):
            columnNumber -= 1
            rem = columnNumber%26 + ord('A')
            columnNumber = columnNumber//26
            answer += chr(rem)
        return answer[::-1]
        
