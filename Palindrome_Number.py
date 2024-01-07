# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        elif x >= 0 and x < 10 :
            return True
        else :
            digit = []
            while x / 10 != 0 :
                digit.append(x % 10)
                x //= 10
            if digit == digit[::-1] :
                return True
            else :
                return False

x = 1234321
t1 = Solution()
print(t1.isPalindrome(x))