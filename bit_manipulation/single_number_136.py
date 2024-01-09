class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        k = nums[0]
        n = len(nums)
        for each in range(1,n):
            k = k ^ nums[each]
        return k
