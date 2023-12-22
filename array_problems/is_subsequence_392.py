from collections import Counter
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n_s = len(s)
        n_t = len(t)
        j=0
        if Counter(s)<= Counter(t):
            for i in range(0,n_t):
                if j>=n_s:
                    return True
                elif s[j] == t[i]:
                    j = j + 1
        if j>=n_s:
            return True
        return False
