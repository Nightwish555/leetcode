class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = []
        for i in nums1:
            for j in range(len(nums2)):
                if i == nums2[j]:
                    a.append(i)
                    nums2.pop(j)
                    break
        return a
