class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap={}
        for index,value in enumerate(order):
            hashmap[value] = index
        for i in range(len(words)-1):
            n = len(words[i+1])
            for j in range(len(words[i])):
                if j>= n:
                    return False
                if words[i][j]!= words[i+1][j]:
                    if hashmap[words[i][j]] > hashmap[words[i+1][j]]:
                        return False
                    break
        return True
