from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> List[str]:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < len(s):
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


ss = ["h", "e", "l", "l", "o"]
print(ss[::-1])
class Excel:

    def __init__(self, sheet_name: str):
        self.sheet_name = sheet_name
        self.sheet = self.get_sheet()
