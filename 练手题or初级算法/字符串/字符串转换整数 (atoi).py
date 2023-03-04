class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        res = ""
        bl = True
        if s[0] == "-":
            s = s[1:]
            bl = False
        for i in s:
            if i.isdigit():
                res += i
        return int(res) if bl else -int(res)


print(Solution().myAtoi("words and 987"))

