class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        count = 1
        print("Number, Count,J,Array")
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1
            if count <=2:
                nums[j] = nums[i]
                j += 1
            print(nums[i],count,j,nums)
        return j



        
