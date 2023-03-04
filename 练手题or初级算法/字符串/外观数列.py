class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'  # 最底层
        cas = self.countAndSay(n - 1)  # 递归
        cas_new = ''  # 新串
        i = 0
        j = 1
        cas += '0'  # 末尾标志，因为不会出现0
        while j < len(cas):

            if cas[i] != cas[j]:
                cas_new += str(j - i) + str(cas[i])
                i = j

            j += 1

        return cas_new
