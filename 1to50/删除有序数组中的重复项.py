from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        slow = 1  # slow在等fast给他数据
        fast = 1  # fast用来找不同给slow
        while fast < n:  # fast遍历完就结束
            if nums[fast] != nums[fast - 1]:  # fast 找到不同的数
                nums[slow] = nums[fast]
                slow += 1  # slow获得fast的数后去下一位等待
            fast += 1

        return slow


if __name__ == '__main__':
    print(Solution().removeDuplicates([1, 1, 2]))
