class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stack = [-1]
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                stack.pop()
                print(stack)
                if not stack:
                    stack.append(i)
                else:

                    res = max(res, i - stack[-1])
        return res


print(Solution().longestValidParentheses(""))
