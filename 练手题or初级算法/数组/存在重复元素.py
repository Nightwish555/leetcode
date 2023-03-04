class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        length = len(nums)
        length1 = len(set(nums))
        if length == length1:
            return False
        else:
            return True
