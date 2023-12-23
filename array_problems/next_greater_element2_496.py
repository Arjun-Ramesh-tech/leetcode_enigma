class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        max_value = nums2[-1]
        result = []
        dictionary = {}
        s = []
        for i in range(len(nums2)):
            dictionary[nums2[i]] = i
            while s and s[-1].get("value") < nums2[i]:
                d = s.pop()
                nums2[d.get("ind")] = nums2[i]
            s.append({"value": nums2[i], "ind": i})
        while s:
            d = s.pop()
            nums2[d.get("ind")] = -1
        for i in range(0,len(nums1)):
            if nums1[i] < nums2[dictionary[nums1[i]]]:
                result.append(nums2[dictionary[nums1[i]]])
            else:
                result.append(-1)
        return result   
