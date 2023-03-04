class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nedLength = len(needle)
        if nedLength == 0:
            return 0
        for k, v in enumerate(haystack):
            if needle[0] == v:
                if needle == haystack[k: k + nedLength]:
                    return k
        return -1

print(Solution().strStr("hello", "ll"))