class Solution:
    def isPalindrome(self, s: str) -> bool:
        pl = [c.lower() for c in s if c.isalnum()] 
        print(pl)
        if pl == pl[::-1]:
            return 1
        return 0
