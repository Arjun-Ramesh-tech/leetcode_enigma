class Solution:
    def minStairs(self,index):
        if index <=1:
            return 0
        if index in self.hash:
            return self.hash[index]
        p = min(self.cost[index-1] + self.minStairs(index-1),self.cost[index-2] + self.minStairs(index-2))
        self.hash[index] = p
        return p
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.cost = cost
        self.hash = {}
        return self.minStairs(len(cost))
        
