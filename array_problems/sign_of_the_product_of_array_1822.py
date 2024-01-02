class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        count = 0
        for each in nums:
            if each<0:
                count += 1
        return 1 if count % 2 == 0 else -1
