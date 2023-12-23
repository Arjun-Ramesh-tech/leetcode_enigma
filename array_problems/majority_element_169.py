import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        val = math.floor(n/2)
        dictionary = {}
        for each in nums:
            if each not in dictionary.keys():
                dictionary[each] = 0
            else:
                dictionary[each] += 1
        for each in dictionary.keys():
            if dictionary[each] >= val:
                return each
