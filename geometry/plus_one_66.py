class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        n = len(digits)
        for i in range(n-1,-1,-1):
            new_val = digits[i] + carry
            digits[i] = new_val%10
            carry = new_val//10
        while carry>0:
            rem = carry%10
            carry = carry//10
            digits.insert(0,rem)
        return digits
