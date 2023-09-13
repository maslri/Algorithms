class Solution:
    def minDeletions(self, s: str) -> int:
        dic = {}
        count = 0
        for char in s :
            try :
                dic[char] += 1
            except KeyError :
                dic[char] = 1
        values = list(dic.values())
        for val in range(1, len(values)) :
             values, count = Solution.calculate_count(values, val, count)
        return count
    
    def calculate_count(values, val, count) :
        while True :
            if values[val] in values[:val] and values[val] != 0:
                    count += 1
                    values[val] -= 1
            else :
                 break
        return values, count

a = Solution()
print(a.minDeletions("bbcebab"))

### ------------------------------------------------------------------------------------- ###

class Solution2:
    def minDeletions2(self, s: str) -> int:
        char_counts = {}
        count = 0
        # Count the frequency of each character
        for char in s:
            char_counts[char] = char_counts.get(char, 0) + 1
        seen_counts = set()
        for char, freq in char_counts.items():
            # Keep decreasing the frequency until it's unique
            while freq in seen_counts:
                freq -= 1
                count += 1
            if freq > 0:
                seen_counts.add(freq)
        return count

a2 = Solution2()
print(a2.minDeletions2("bbcebab"))