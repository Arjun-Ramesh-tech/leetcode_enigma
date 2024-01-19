class Solution:
    def __init__(self):
        self.paranthesis = []
    def generator(self,open_p,close_p,n,string):
        if n == close_p and n== open_p:
            self.paranthesis.append(string)
            return
        if n < close_p or n < open_p or close_p>open_p:
            return
        if n > close_p:
            self.generator(open_p,close_p+1,n,string+")")
        if n > open_p:
            self.generator(open_p+1,close_p,n,string+"(")
    def generateParenthesis(self, n: int) -> List[str]:
        self.generator(0,0,n,"")
        return self.paranthesis

        
