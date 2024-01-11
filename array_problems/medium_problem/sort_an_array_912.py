class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums):
            n = len(nums)
            if n>1:
                middle = n//2
                left_array = mergeSort(nums[:middle])
                right_array = mergeSort(nums[middle:])
                i = j = k =0
                while i<middle and j <n-middle:
                    if left_array[i] <= right_array[j]:
                        nums[k] = left_array[i]
                        k = k + 1
                        i = i + 1
                    else:
                        nums[k] = right_array[j]
                        k = k + 1
                        j = j + 1
                while i <middle:
                    nums[k] = left_array[i]
                    k = k + 1
                    i = i + 1
                while j <(n-middle):
                    nums[k] = right_array[j]
                    k = k + 1
                    j = j + 1
                #print(left_array,right_array,nums,middle,n-middle)
                return nums
            return nums
        return mergeSort(nums)
        
