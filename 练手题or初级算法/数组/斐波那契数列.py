class Solution:
    def fib(self, n: int) -> int:
        a, b, = 0, 1
        for i in range(n):
            a, b = b, a + b
        return int(a % 1000000007)


def fib2(q):
    if q == 1 or q == 2:
        return 1
    return int(fib2(q - 1) + fib2(q - 2) % 1000000007)


print(fib2(8))
