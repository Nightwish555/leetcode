class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x1 = str(x)[::-1]
        if int(x1) == x:
            return True
        return False


if __name__ == '__main__':
    x = -123
    print(str(x)[::-1].isalnum())
