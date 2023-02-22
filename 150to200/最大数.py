from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if str(nums[i]) + str(nums[j]) < str(nums[j]) + str(nums[i]):
                    nums[i], nums[j] = nums[j], nums[i]
        s = ""
        for num in nums:
            s += str(num)
        return str(int(s))