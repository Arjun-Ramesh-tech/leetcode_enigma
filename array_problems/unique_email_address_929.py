class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_email = []
        for each in emails:
            each_split = each.split('@')
            each_split[0] = each_split[0].replace(".","")
            for i in range(0,len(each_split[0])):
                if each_split[0][i] == '+':
                    each_split[0] = each_split[0][:i]
                    break
            unique_email.append(each_split[0]+'@'+each_split[1])
        return len(set(unique_email))

        
