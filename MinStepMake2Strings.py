# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/?envType=daily-question&envId=2024-01-13

import time

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = 0
        list_a = list(s)
        for i in t :
            if i in list_a :
                list_a.remove(i)
            else :
                count += 1
        return count
    
    def minSteps2(self, s: str, t: str) -> int:
        count = 0
        char_count = {}

        # Count characters in string s
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Decrement counts based on characters in string t
        for char in t:
            if char in char_count:
                char_count[char] -= 1
            else:
                count += 1

        return count
    
s = "example_s"
t = "example_t"

# Create an instance of the class
solution_instance = Solution()

# Measure the time taken by method 1
start_time = time.time()
solution_instance.minSteps(s, t)
end_time = time.time()
time_method1 = end_time - start_time

# Measure the time taken by method 2
start_time = time.time()
solution_instance.minSteps2(s, t)
end_time = time.time()
time_method2 = end_time - start_time

# Compare the times
print(f"Time taken by method 1: {time_method1} seconds")
print(f"Time taken by method 2: {time_method2} seconds")

# Time taken by method 1: 31.699193477630615 seconds
# Time taken by method 2: 0.005981922149658203 seconds