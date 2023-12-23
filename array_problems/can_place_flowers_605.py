class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        y = len(flowerbed)
        if y==1 and flowerbed[0] == 0:
            return 1>=n
        elif y==1 and flowerbed[0] == 1:
            return 0>=n
        for i in range(0, y):
            if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i]=1
                count += 1
            elif i == y-1 and flowerbed[i] == 0 and flowerbed[i-1] == 0:
                flowerbed[i]=1
                count += 1
            elif ((i+1) < y) and ((i-1) >=0) and flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                flowerbed[i]=1
                count += 1
        return count >= n
        
