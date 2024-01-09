class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = len(num)
        carry = k
        for i in range(n-1,-1,-1):
            carry = num[i] + carry
            num[i] = carry % 10
            carry = carry//10
        while(carry>0):
            rem = carry%10
            carry = carry//10
            num.insert(0,rem)
        return num
