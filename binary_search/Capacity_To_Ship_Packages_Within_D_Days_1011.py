class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left,right = max(weights),sum(weights)
        while left!=right:
            middle, capacity, day = int((left+right)/2), 0, 1
            for i in weights:
                capacity += i
                if capacity > middle:
                    day += 1
                    capacity = i
            if day <= days:
                right = middle
            else:
                left = middle + 1
        return left
