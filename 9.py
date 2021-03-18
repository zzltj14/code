class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        y = 0
        s = x
        while s > 0:
            y = y*10 + s%10
            s = int(s/10)
        if x == y:
            return True
        else:
            return False

test = Solution()
print(test.isPalindrome(10))