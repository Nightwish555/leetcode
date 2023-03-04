# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        count = 0
        q = [[root]]
        while q != [[]]:
            count += 1
            cur_node = q.pop(0)
            s = []
            for i in cur_node:
                if i.left:
                    s.append(i.left)
                if i.right:
                    s.append(i.right)
            q.append(s)
        return count


def quick_sort(data: list):
    if len(data) == 0:
        return data
    mid = data[len(data) // 2]
    data.remove(mid)
    left = []
    right = []
    for i in data:
        if i < mid:
            left.append(i)
        if i > mid:
            right.append(i)
    return quick_sort(left) + mid + quick_sort(right)


def bubbleSort(data: list):
    length = len(data)
    for i in range(length - 1):
        for j in range(length - i - 1, length):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


def two_search(data: list, target: int):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] > target:
            right = mid - 1
        if data[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1
