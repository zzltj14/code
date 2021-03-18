class Solution:
    def reverse(self, x: int) -> int:
        y = 0
        isneg =0
        if x < 0:
            isneg = 1
            x = -1*x
        while x != 0:
            y = y*10 + x%10
            x = int(x/10)
            if y > 2147483647 or y < -2147483648:
                return 0
        if isneg == 1:
            return -1*y
        else:
            return y

test = Solution()
print(test.reverse(120))