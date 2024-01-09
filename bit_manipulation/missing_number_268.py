class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        k = len(nums)
        for index,value in enumerate(nums):
            k ^= index ^ value
        return k
