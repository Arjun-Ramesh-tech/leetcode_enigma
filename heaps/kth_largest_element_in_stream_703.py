import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        self.arr = nums[:k]
        heapify(self.arr)
        for i in range(k,len(nums)):
            if nums[i] > self.arr[0]:
                heappushpop(self.arr,nums[i])

    def add(self, val: int) -> int:
        if len(self.arr) < self.k:
            heappush(self.arr,val)
        elif val > self.arr[0]:
            heappushpop(self.arr,val)
        return self.arr[0]




# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
