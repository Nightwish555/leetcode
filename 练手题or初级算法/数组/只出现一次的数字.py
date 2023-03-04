from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return sum(set(nums)) * 2 - sum(nums)

    def singleNumberV1(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i < len(nums):
            if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i = i + 2
            else:
                return nums[i]
        return nums[len(nums) - 1]


print(Solution().singleNumberV1([4, 1, 2, 1, 2]))
