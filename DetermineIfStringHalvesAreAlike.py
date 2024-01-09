# https://leetcode.com/problems/determine-if-string-halves-are-alike/description/?envType=daily-question&envId=2024-01-10

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        count_vowels_a = 0
        count_vowels_b = 0
        a = s[:len(s)//2]
        b = s[len(s)//2:]
        for i in range(len(s)//2) :
            if a[i] in vowels :
                count_vowels_a += 1
            if b[i] in vowels :
                count_vowels_b += 1
        if count_vowels_a == count_vowels_b :
            return True
        else :
            return False
        



r = Solution()
print(r.halvesAreAlike("textbook"))
print(r.halvesAreAlike("book"))