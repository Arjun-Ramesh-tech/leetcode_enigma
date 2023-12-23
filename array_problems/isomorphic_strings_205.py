class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        complete_dict = {}
        if len(s)== len(t):
            for each_index in range(0,len(s)):
                if s[each_index] == t[each_index] and s[each_index] not in complete_dict.keys():
                    if s[each_index] not in complete_dict.values():
                        complete_dict[s[each_index]] = s[each_index]
                    else:
                        return False
                elif s[each_index] == t[each_index] and complete_dict[s[each_index]] != t[each_index]:
                    return False
                elif s[each_index] != t[each_index] and s[each_index] not in complete_dict.keys():
                    if t[each_index] not in complete_dict.values():
                        complete_dict[s[each_index]] = t[each_index]
                    else:
                        return False
                elif s[each_index] != t[each_index] and complete_dict[s[each_index]] != t[each_index]:
                    return False
        else:
            return False
        return True
