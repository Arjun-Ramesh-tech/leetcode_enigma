import heapq
from collections import defaultdict
class slidingWindow:
    
    def __init__(self):
        self.left_array_max_heap = []
        self.right_array_min_heap = []
        heapq.heapify(self.left_array_max_heap)
        heapq.heapify(self.right_array_min_heap)
        self.balance = 0
        self.invalidated_elements = defaultdict(int)

    def add(self, num):
        if self.left_array_max_heap and num <= -self.left_array_max_heap[0]:
            heapq.heappush(self.left_array_max_heap,-num)
            self.balance -= 1
        else:
            heapq.heappush(self.right_array_min_heap,num)
            self.balance += 1
        self.rebalance()

    def rebalance(self):
        if self.balance>0:
            while self.balance>0 and self.right_array_min_heap:
                temp = heapq.heappop(self.right_array_min_heap)
                if self.invalidated_elements[temp]>0:
                    self.invalidated_elements[temp] -= 1
                else:
                    heapq.heappush(self.left_array_max_heap,-temp)
                    self.balance -=2
        elif self.balance<0:
            while self.balance<0 and self.left_array_max_heap:
                temp = -heapq.heappop(self.left_array_max_heap)
                if self.invalidated_elements[temp]>0:
                    self.invalidated_elements[temp] -= 1
                else:
                    heapq.heappush(self.right_array_min_heap,temp)
                    self.balance +=2
    
    def check_top(self):
        while self.left_array_max_heap and (-self.left_array_max_heap[0] in self.invalidated_elements.keys()) and (self.invalidated_elements[-self.left_array_max_heap[0]]>0):
            self.invalidated_elements[-self.left_array_max_heap[0]] -=1
            heapq.heappop(self.left_array_max_heap)
        while self.right_array_min_heap and (self.right_array_min_heap[0] in self.invalidated_elements.keys()) and (self.invalidated_elements[self.right_array_min_heap[0]]>0):
            self.invalidated_elements[self.right_array_min_heap[0]] -=1
            heapq.heappop(self.right_array_min_heap)

    def remove(self,num):
        if num==-self.left_array_max_heap[0]:
            heapq.heappop(self.left_array_max_heap)
            self.balance += 1
        elif num == self.right_array_min_heap[0]:
            heapq.heappop(self.right_array_min_heap)
            self.balance -= 1
        elif num > -self.left_array_max_heap[0]:
            self.balance -= 1
            self.invalidated_elements[num] += 1
        else:
            self.balance += 1
            self.invalidated_elements[num] += 1
        self.rebalance()

    def get_median(self):
        self.check_top()
        if self.balance ==0:
            return (-self.left_array_max_heap[0] + self.right_array_min_heap[0])/2
        elif self.balance >0:
            return self.right_array_min_heap[0]
        else:
            return -self.left_array_max_heap[0]

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        result = []
        n = len(nums)
        median = slidingWindow()
        for i in range(k):
            median.add(nums[i])
        result.append(median.get_median())
        for i in range(k,n):
            median.add(nums[i])
            median.remove(nums[i-k])
            result.append(median.get_median())
        return result
