'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def recursion(current,front,end):
            if n == front and n == end:
                result.append(current)
                return
            if front > n or end > n or front < end:
                return 
            recursion(current + '(', front + 1, end)
            recursion(current + ')', front, end + 1)
            return
        recursion("",0,0)
        return set(result)
        