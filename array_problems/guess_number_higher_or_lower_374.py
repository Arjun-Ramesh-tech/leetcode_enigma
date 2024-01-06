# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        i = 1
        j = n
        while(1):
            middle = int((i + j) / 2)
            choice = guess(middle)
            if choice == 0:
                return middle
            elif choice == 1:
                i = middle + 1
            else:
                j = middle - 1
