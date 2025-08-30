from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return self.subsetXOR(nums, 0, 0)

    def subsetXOR(self, nums: List[int], index: int, current_xor: int) -> int:
        if index == len(nums):
            return current_xor
        return self.subsetXOR(nums, index + 1, current_xor) + self.subsetXOR(
            nums, index + 1, current_xor ^ nums[index]
        )


test = Solution()
print(test.subsetXORSum([1, 3]))
print(test.subsetXORSum([5, 1, 6]))
print(test.subsetXORSum([3, 4, 5, 6, 7, 8]))
