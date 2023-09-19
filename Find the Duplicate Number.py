# https://leetcode.com/problems/find-the-duplicate-number/description/

from typing import List

class Solution:

    def findDuplicate(self, nums: List[int]) -> int:
        # Step 1: Initialize slow and fast pointers
        slow = nums[0]
        fast = nums[0]
        # Step 2: Find the meeting point inside the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # Step 3: Reset one pointer to the beginning
        fast = nums[0]
        # Step 4: Move both pointers until they meet at the start of the cycle
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


nums1 = [1, 3, 4, 2, 2]
nums2 = [3, 1, 3, 4, 2]

a = Solution()

result1 = a.findDuplicate(nums1)
print(result1)

result2 = a.findDuplicate(nums2)
print(result2)