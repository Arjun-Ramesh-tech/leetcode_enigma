from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = Counter(text)
        return min(counter['b'],counter['a'],counter['n'],counter['o']//2,counter['l']//2)      
