class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1,len(strs)):
            n = min(len(strs[i]),len(prefix))
            for x in range(0,n):
                if prefix[x] !=strs[i][x]:
                    prefix = prefix[:x]
                    break
            if len(strs[i]) < len(prefix):
                prefix = prefix[:len(strs[i])]
        return prefix
