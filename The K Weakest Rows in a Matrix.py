## https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/

from typing import List

# value_if_true if condition else value_if_false
# new_list = [expression for item in iterable]


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        in_list = [sum(x for x in i if x == 1) for i in mat]
        sorted_list = sorted(enumerate(in_list), key=lambda x: (x[1], x[0]))
        return [item[0] for item in sorted_list][:k]


in_list =   [[1,0,0,0],
            [1,1,1,1],
            [1,0,0,0],
            [1,0,0,0]]
k = 2

a = Solution()
print(a.kWeakestRows(in_list, k))
# The rows ordered from weakest to strongest are [0,2,3,1].


