import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapify(stones)
        n = len(stones)
        while n>=2:
            a,b = heappop(stones)*-1,heappop(stones)*-1
            if a!=b:
                heappush(stones,-(a-b))
                n -= 1
            else:
                n -= 2
        if n == 0:
            return 0
        return stones[0]*-1
