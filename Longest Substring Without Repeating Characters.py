# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

class Solution:
    def lengthOfLongestSubstring(self, s):
        if s == "":
            return 0
        tmp = []
        count = {}
        keyCount = 0
        index = 0
        while True:
            char = s[index]
            if char in tmp:
                keyCount += 1
                tmp.clear()
                ss = str(s[:index])
                inn = ss.rfind(char)
                index = inn + 1
                del ss
                del inn
                continue
            try:
                count[keyCount] += 1
            except KeyError as e:
                count[keyCount] = 1
            tmp.append(char)
            index += 1
            if index == len(s):
                break
        return max(count.values())


t1 = Solution()
print(t1.lengthOfLongestSubstring("dvdf"))
