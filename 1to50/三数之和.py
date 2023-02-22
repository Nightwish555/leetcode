from itertools import combinations
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        L = []
        for i in combinations(nums, 3):
            if sum(list(i)) == 0:
                L.append(list(i))
        L1 = []
        for j in L:
            j.sort()
            L1.append(j)
        b = list(set([tuple(j) for j in L1]))
        return [list(i) for i in b]


nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))
