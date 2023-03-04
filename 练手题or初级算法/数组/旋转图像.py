from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 或者 先上下交换 再按照对角线交换
        j = 0
        for i in zip(*matrix[::-1]):
            matrix[j] = i
            j += 1


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(*matrix[::-1])
for i in zip(*matrix[::-1]):
    print(i)
