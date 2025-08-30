from typing import List


def maxFrequencyElements(nums: List[int]) -> int:
    dc = {}
    for num in nums:
        try:
            dc[num] += 1
        except KeyError:
            dc[num] = 1
    return sum([y for x, y in dc.items() if y == max(dc.values())])


print(maxFrequencyElements([1, 2, 2, 3, 1, 4]))
print(maxFrequencyElements([1, 2, 3, 4, 5]))
