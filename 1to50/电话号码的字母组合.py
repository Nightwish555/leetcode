class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        KEY = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}

        if len(digits) == 0:
            return []

        res_list = []

        def dfs(digits: str, res: str):
            if len(digits) == 0:
                res_list.append(res)  # 搜索叶子结点，返回上一级
            else:
                for val in KEY[digits[0]]:  # 搜索子节点
                    dfs(digits[1:], res + val)

        dfs(digits, '')

        return res_list
