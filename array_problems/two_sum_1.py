class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i in range(0,len(nums)):
            if nums[i] in store:
                return [store[nums[i]],i]
            store[target-nums[i]] = i
