from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_value = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                if nums[i] > nums[j]:
                    for k in range(j + 1, len(nums)):
                        max_value = max(max_value, self.TripleValue(i, j, k, nums))
        return max_value

    def TripleValue(self, i: int, j: int, k: int, nums: List[int]) -> int:
        return (nums[i] - nums[j]) * nums[k]


test = Solution()
print(test.maximumTripletValue([12, 6, 1, 2, 7]))
print(test.maximumTripletValue([1, 10, 3, 4, 19]))
print(test.maximumTripletValue([1, 2, 3]))
