from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        map = dict()
        for i in range(length):
            t = target - nums[i]
            if map.get(t) is None:
                map[nums[i]] = i
            else:
                return i, map.get(t)
