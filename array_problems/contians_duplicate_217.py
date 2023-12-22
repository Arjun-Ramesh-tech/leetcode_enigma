class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_ele = set(nums)
        if len(unique_ele) == len(nums):
            return False
        else:
            return True
