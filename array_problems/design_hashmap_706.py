class MyHashMap:

    def __init__(self):
        self.key = []
        self.value = []
        self.size = 0

    def put(self, key: int, value: int) -> None:
        if key not in self.key:
            self.key.append(key)
            self.value.append(value)
            self.size += 1
        else:
            for i in range(0,self.size):
                if key == self.key[i]:
                    self.value[i] = value
                    break


    def get(self, key: int) -> int:
        if key not in self.key:
            return -1
        for i in range(0,self.size):
            if self.key[i] == key:
                return self.value[i]

    def remove(self, key: int) -> None:
        if key in self.key:
            for i in range(0,self.size):
                if key == self.key[i]:
                    del self.key[i]
                    del self.value[i]
                    break



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
