from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> list:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        length = len(nums)
        nums1 = nums.copy()

        for key, v in enumerate(nums):
            kk = key + k
            if kk < length:

                nums1[kk] = v
            else:

                nums1[abs(length - kk)] = v

        return nums1


print(Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3))



