from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums).most_common()
        result = []
        for i in range(k):
            result.append(count[i][0])
        return result
