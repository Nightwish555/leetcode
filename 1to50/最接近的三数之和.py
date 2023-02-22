class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        temp = 0
        for i in range(length):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = length - 1
            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                if temp == target:
                    return temp
                if temp > target:
                    # 如果和大于 target，移动 c 对应的指针
                    k0 = right - 1
                    # 移动到下一个不相等的元素
                    while left < k0 and nums[k0] == nums[right]:
                        k0 -= 1
                    right = k0
                else:
                    # 如果和小于 target，移动 b 对应的指针
                    j0 = left + 1
                    # 移动到下一个不相等的元素
                    while j0 < right and nums[j0] == nums[left]:
                        j0 += 1
                    left = j0
        return temp
