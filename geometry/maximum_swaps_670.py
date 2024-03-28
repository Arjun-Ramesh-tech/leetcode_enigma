class Solution:
    def maximumSwap(self, num: int) -> int:
        list_num = list(str(num))
        n = len(list_num)
        flag = False
        for i in range(n):
            max_value =-1
            max_index = -1
            for j in range(i+1,n):
                if int(list_num[i]) < int(list_num[j]):
                    if max_value<=int(list_num[j]):
                        max_value = int(list_num[j])
                        max_index = j
            if not (max_value == -1):
                temp = list_num[i]
                list_num[i] = str(max_value)
                list_num[max_index] = temp
                break 
        return int(''.join(list_num))

        
