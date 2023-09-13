class Solution:
    # def isValid(self, s: str) -> bool:
    def isValid(self, s: str) -> bool:
        in_list = []
        dic = {")" : "(", "}" : "{", "]" : "["}
        index = 0
        while True :
            if s[index] in dic.keys() :
                try :
                    if in_list[-1] == dic[s[index]] :
                        in_list.pop()
                    else :
                        return False
                except IndexError :
                    return False
            else :
                in_list.append(s[index])
            index += 1
            if index == len(s) :
                if len(in_list) == 0 :
                    return True
                else :
                    return False
                
a = Solution()
print(a.isValid("]"))