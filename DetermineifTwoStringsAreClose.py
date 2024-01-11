# https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=daily-question&envId=2024-01-14

class Solution:
    
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2) :
            return False
        if Solution._checkSwap(word1, word2) and Solution._checkTransform(word1, word2) and Solution._checkTransform(word2, word1) :
            return True
        return False

    def _checkSwap(word1 : str, word2 : str) -> bool :
        for i in word1 :
            if i not in word2 :
                return False
        return True
        
    def _checkTransform(word1 : str, word2 : str) -> bool :
        char_count1 = {}
        char_count2 = {}

        for char in word1:
            char_count1[char] = char_count1.get(char, 0) + 1

        for char in word2:
            char_count2[char] = char_count2.get(char, 0) + 1

        freq1 = sorted(char_count1.values())
        freq2 = sorted(char_count2.values())

        return freq1 == freq2
        
r = Solution()

print(r.closeStrings("abc", "bca"))
print(r.closeStrings("a", "aa"))
print(r.closeStrings("cabbba", "abbccc"))
print(r.closeStrings("abbbzcf", "babzzcz"))
print(r.closeStrings("aaabbbbccddeeeeefffff", "aaaaabbcccdddeeeeffff"))
