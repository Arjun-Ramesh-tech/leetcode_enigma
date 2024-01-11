class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset= set(nums)
        longest_streak = 0
        for i in nums:
            if i-1 not in hashset:
                current_streak = 1
                value = i + 1
                while(value in hashset):
                    current_streak += 1
                    value += 1
                longest_streak = max(longest_streak,current_streak)
        return longest_streak
