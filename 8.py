class Solution:
    def myAtoi(self, s: str) -> int:
        try:
            index = 0
            n = len(s)
            a = "+-0123456789"
            b = "0123456789"
            posFlag = 1
            while s[index] == " ":
                index += 1
            if s[index] not in a:
                return 0
            elif s[index] == "+":
                posFlag = 1
                index += 1
            elif s[index] == "-":
                posFlag = -1
                index += 1
            yStart = index
            if s[index] not in b:
                return 0
            while index < n and s[index] in b:
                index += 1
            yEnd = index
            y = posFlag * int(s[yStart:yEnd])
            if y > 2147483647:
                y = 2147483647
            elif y < -2147483648:
                y = -2147483648
            return y

        except:
            return 0

        # index = 0
        # n = len(s)
        # a = "+-0123456789"
        # posFlag = 1
        # while s[index] == " ":
        #     index += 1
        # if s[index] not in a:
        #     return 0
        # elif s[index] == "+":
        #     posFlag = 1
        #     index += 1
        # elif s[index] == "-":
        #     posFlag = -1
        #     index += 1
        # yStart = index
        # while index < n and s[index] in a:
        #     index += 1
        # yEnd = index
        # y = posFlag * int(s[yStart:yEnd])
        # if y > 2147483647:
        #     y = 2147483647
        # elif y < -2147483648:
        #     y = -2147483648
        # return y

test = Solution()
print(test.myAtoi("+-2"))

