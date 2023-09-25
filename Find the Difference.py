# https://leetcode.com/problems/find-the-difference/description/?envType=daily-question&envId=2023-09-25

class Solution:

    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0 :
            return t
        for i in t :
            if s.count(i) != t.count(i) :
                return i


s = "a"
t = "aa"

a = Solution()
print(a.findTheDifference(s, t))