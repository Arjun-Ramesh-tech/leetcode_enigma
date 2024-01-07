class Solution:
    def isValid(self, s: str) -> bool:
        open_paran = ['(','{','[']
        stack = []
        for i in s:
            if i in open_paran:
                stack.append(i)
            elif len(stack) > 0:
                k = stack.pop()
                if not ((k =='(' and i == ')') or (k =='[' and i == ']') or (k =='{' and i == '}')):
                    return False
            else:
                return False
        if len(stack)==0:
            return True
        return False

            

