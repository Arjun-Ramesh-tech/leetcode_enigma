from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = defaultdict(list)
        result = []
        n = len(strs)
        for i in range(n):
            data[''.join(sorted(strs[i]))].append(i)
        k = 0
        for each in data.keys():
            result.append([])
            for i in data[each]:
                result[k].append(strs[i])
            k = k + 1
        return result
