class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0]*n
        answer[0] = 1
        right = 1
        for i in range(1,n):
            answer[i] = answer[i-1] * nums[i-1]
        for i in range(n-1,-1,-1):
            answer[i] = answer[i]*right
            right = right * nums[i]
        return answer
        
