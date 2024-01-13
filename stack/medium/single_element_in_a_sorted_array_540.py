class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left,right = 0,len(nums)-1
        if right==0:
            return nums[0]
        while right-left>3:
            mid = (right+left)//2
            if mid%2 == 0:
                if nums[mid] == nums[mid-1]:
                    right = mid
                elif nums[mid] == nums[mid+1]:
                    left = mid
                else:
                    return nums[mid]
            elif nums[mid] == nums[mid-1]:
                left = mid + 1
            elif nums[mid] == nums[mid+1]:
                right = mid-1
            else:
                return nums[mid]
        return nums[left]^ nums[left+1]^ nums[left+2]
