from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    if not str:
        return ""
    s1 = min(strs)
    s2 = max(strs)
    for i, x in enumerate(s1):
        if x != s2[i]:
            return s2[:i]
    return s1



