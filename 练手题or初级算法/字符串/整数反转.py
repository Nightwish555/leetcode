class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        while x != 0:
            tmp = x % 10
            new_res = res * 10 + tmp
            if (new_res - tmp) / 10 != res:
                return 0
            res = res * 10 + x % 10
            x //= 10
            print(x)
        return res


Solution().reverse(123)