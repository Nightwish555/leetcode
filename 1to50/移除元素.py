from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ix = 0
        while True:
            if ix + 1 > len(nums):
                break

            a = nums[ix]

            if a == val:
                nums.pop(ix)
            else:
                ix += 1

        return len(nums)


if __name__ == '__main__':
    print(Solution().removeElement([3, 2, 2, 3], 3))
