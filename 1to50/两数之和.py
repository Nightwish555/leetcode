from typing import List


class Solution:

    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        length = len(nums)
        if length < 2:
            return []
        for k, v in enumerate(nums):

            for j in range(k + 1, length):
                if v + nums[j] == target:
                    return [k, j]
        return []


if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    print(Solution.twoSum(nums, target))
