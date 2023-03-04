from typing import List

res = []


def perm(elem_list, s=''):

    # 参数合法性检查
    if len(elem_list) == 0:
        return
    # 跳出条件
    if len(elem_list) == 1:
        # 打印当前结果
        res.append(s + elem_list[0])
        return
    # 依次挑选一个元素作为第1元素
    for i, e in enumerate(elem_list):
        # 递归调用自身，同时传入当前的前缀字符串
        perm(elem_list[:i] + elem_list[i + 1:], s + e)


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        perm(words)
        return [s.find(i) for i in res if s.find(i) != -1]


w = ["bar", "foo", "the"]

perm(w)
print(res)
s = "barfoofoobarthefoobarman"
print([s.find(i) for i in res if s.find(i) != -1])
