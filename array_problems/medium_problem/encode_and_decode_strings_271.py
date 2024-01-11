class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        result = ""
        for i in strs:
            result += str(len(i)) + '$' + i
        return result
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        n = len(s)
        if n ==0:
            return []
        answer=[]
        while(i<n):
            start = i
            while(s[i]!='$'):
                i = i + 1
            length_of_string = int(s[start:i])
            i = i + 1
            answer.append(s[i:i+length_of_string])
            i = i + length_of_string
        return answer
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
