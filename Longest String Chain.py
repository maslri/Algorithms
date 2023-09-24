# https://leetcode.com/problems/longest-string-chain/description/

from typing import List
from numpy import arange

class Solution :

    def longestStrChain(self, words: List[str]) -> int:
        
        word_set = set(words)
        max_chain = 1
        for word in words:
            max_chain = max(max_chain, self.findLongestChain(word, word_set))
        return max_chain
    
    def findLongestChain(self, word: str, word_set: set) -> int:
            max_chain = 1
            for i in range(len(word)):
                new_word = word[:i] + word[i+1:]
                if new_word in word_set:
                    max_chain = max(max_chain, 1 + self.findLongestChain(new_word, word_set))
            return max_chain

class Solution2 :

    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)  # Sort the words by length
        dp = {}  # Dictionary to store the longest chain length for each word       
        max_chain = 1  # Minimum chain length is 1 (the word itself)
        
        for word in words:
            max_chain_for_word = 1
            for i in range(len(word)):
                prev_word = word[:i] + word[i+1:]  # Remove one character
                if prev_word in dp:
                    max_chain_for_word = max(max_chain_for_word, dp[prev_word] + 1)
            dp[word] = max_chain_for_word
            max_chain = max(max_chain, max_chain_for_word)
        
        return max_chain

class Solution3 :
     def longestStrChain(self, words):
        dp = {}
        for w in sorted(words, key=len):
            dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in arange(len(w)))
        return max(dp.values())

class Solution4 :
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = {}
        max_chain = 0
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                prev_word = word[:i] + word[i+1:]
                if prev_word in dp:
                    dp[word] = max(dp[word], dp[prev_word] + 1)
            max_chain = max(max_chain, dp[word])
        return max_chain

# Test cases
a = Solution()
b = Solution2()
c = Solution3()
d = Solution4()
print(a.longestStrChain(["a","b","ba","bca","bda","bdca"]))  # Output: 4
print(b.longestStrChain(["a","b","ba","bca","bda","bdca"]))  # Output: 4
print(c.longestStrChain(["a","b","ba","bca","bda","bdca"]))  # Output: 4
print(d.longestStrChain(["a","b","ba","bca","bda","bdca"]))  # Output: 4
print("------------------------------------")
print(a.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))  # Output: 5
print(b.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))  # Output: 5
print(c.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))  # Output: 5
print(d.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))  # Output: 5
print("------------------------------------")
print(a.longestStrChain(["abcd","dbqca"]))  # Output: 1
print(b.longestStrChain(["abcd","dbqca"]))  # Output: 1
print(c.longestStrChain(["abcd","dbqca"]))  # Output: 1
print(d.longestStrChain(["abcd","dbqca"]))  # Output: 1

