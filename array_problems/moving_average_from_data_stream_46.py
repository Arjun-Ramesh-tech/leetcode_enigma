class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.iter = 0
        self.sum = 0
        self.values = []

    def next(self, val: int) -> float:
        self.iter +=1
        self.values.append(val)
        if self.iter-1<self.size:
            self.sum += val
            return self.sum/self.iter
        else:
            self.sum = self.sum + val - self.values[0]
            self.values.pop(0)
            return self.sum/self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
