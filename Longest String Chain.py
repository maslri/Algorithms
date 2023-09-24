# https://leetcode.com/problems/longest-string-chain/description/

from typing import List

class Solution:

    count = 0
    
    def longestStrChain(self, words: List[str]) -> int:
        if len(words) == 1 :
            return 1
              
        min_list = [s for s in words if len(s) == len(min(words, key=len))]
        words = [x for x in words if x not in min_list]

        for min_l in min_list :
            self.change_list(min_l, words)
        return self.count

    def change_list(self, min_l : str, words : List[str]) -> None :
        if not words :
            return self.count
        
        min_list = [i for i in words if len(i) == len(min_l) + 1]

        for min_ll in min_list :
            if self.isPredecessor(min_l, min_ll) :
                self.count += 1
                self.change_list(min_ll, words)
        else :
            words = [x for x in words if x not in min_list]
    
    def isPredecessor(self, a : str, b : str) -> bool :
        valid = 0
        for i in a :
            check = b.find(i)
            if valid > check :
                return False
            else :
                valid = check
                del(check)
        else :
            return True


a = Solution()
print(a.longestStrChain(["a","b","ba","bca","bda","bdca"]))
#print(a.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))
#print(a.longestStrChain(["abcd","dbqca"]))

