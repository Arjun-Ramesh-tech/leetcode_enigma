class Solution:
    def check_palindrome(self,s,i,j):
        while(i<j):
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return [i,j,False]
        return [-1,-1,True]
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        return_list = self.check_palindrome(s,i,j)
        if return_list[0] == -1:
            return True
        else:
            return self.check_palindrome(s,return_list[0]+1,return_list[1])[2] or self.check_palindrome(s,return_list[0],return_list[1]-1)[2]
