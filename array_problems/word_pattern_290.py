class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.strip(' ').split(' ')
        hashmap = {}
        if len(pattern) != len(s):
            return 0
        string_index = 0
        for each_char in pattern:
            if each_char not in hashmap and s[string_index] not in hashmap.values():
                hashmap[each_char] = s[string_index]
            elif each_char not in hashmap and s[string_index] in hashmap.values():
                return 0
            elif s[string_index] != hashmap[each_char]:
                return 0
            string_index += 1 
        return 1
        
