class Solution:

    @staticmethod
    def reverse(x: int) -> int:
        s = str(x)
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        if s.startswith('-'):
            l = s[1:][::-1]
            return -int("".join(l)) if INT_MIN < int("".join(l)) < INT_MAX else 0
        else:
            l = s[::-1]
            return int("".join(l)) if INT_MIN < int("".join(l)) < INT_MAX else 0



