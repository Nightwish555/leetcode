class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, j, k = n - 2, n - 1, n - 1

        while i >= 0:
            if nums[i] < nums[j]:
                break
            else:
                i -= 1
                j -= 1
        if i == -1:
            nums.reverse()
        else:
            while k >= j:
                if nums[i] < nums[k]:
                    break
                else:
                    k -= 1
            nums[i], nums[k] = nums[k], nums[i]
            # print([1,2,3].reverse())
            num = nums[j:]
            num.reverse()
            nums[j:] = num
