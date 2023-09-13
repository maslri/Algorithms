class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target) :
        num_dict = {}
        for i, num in enumerate(nums) :
            complement = target - num
            if complement in num_dict:
                return num_dict[complement], i
            num_dict[num] = i

a = Solution()

list = [2, 3, 4, 5, 6]
print(a.twoSum(list, 7))