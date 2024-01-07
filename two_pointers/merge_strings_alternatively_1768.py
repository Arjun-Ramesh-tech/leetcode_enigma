class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        match = min(n1,n2)
        i = 0
        new_str = ""
        while i< match:
            new_str += word1[i]+ word2[i]
            i += 1
        if n1==i:
            return new_str + word2[i:]
        return new_str + word1[i:]
        
