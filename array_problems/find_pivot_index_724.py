class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = 0
        left_array = []
        insert_value = 0
        for each_num in nums:
            total_sum = total_sum + each_num
            left_array.append(insert_value)
            insert_value = insert_value + each_num
        for index in range(0,len(nums)):
            if left_array[index] == total_sum-nums[index] - left_array[index]:
                return index
        return -1   
