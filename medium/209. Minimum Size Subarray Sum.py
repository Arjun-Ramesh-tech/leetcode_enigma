'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end, n, current_sum, best_length = 0, 0, len(nums), 0, len(nums) + 1
        for end in range(n):
            current_sum += nums[end]
            while current_sum >=target:
                best_length, current_sum, start = min(best_length,end-start+1), current_sum-nums[start], start + 1
        return best_length if best_length!=len(nums) + 1 else  0