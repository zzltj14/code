# 本题需要在s，p前各加一个奇异字符，既不影响后面字符的匹配，又可避免考虑空字符串的边界条件。
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = " " + s
        p = " " + p
        len_s = len(s)
        len_p = len(p)
        if len_p == 1:
            if len_s == 1:
                return True
            else:
                return False
        f = [[0 for _ in range(len_p)]  for _ in range(len_s)]
        f[0][0] = 1
        if len_s == 1:
            if len_p%2 == 0:
                return False
            else:
                j = 2
                while j<=len_p-1 and p[j] =="*":
                    j += 2
                if j > len_p-1:
                    return True
                else:
                    return False

        f[0][1] = 0
        j = 0
        for i in range(1,len_s):
            f[i][0] = 0
        j = 1
        if s[1] == p[1] or p[1] == ".":
            f[1][1] = 1
        else:
            f[1][1] = 0
        for i in range(2,len_s):
            f[i][1] = 0
        i = 0
        for j in range(2,len_p):
            if p[j] != "*":
                f[0][j] = 0
            else:
                f[0][j] = f[0][j-2]
        for i in range(1,len_s):
            for j in range(2,len_p):
                if p[j] != "*":
                    if s[i] == p[j] or p[j] == ".":
                        f[i][j] = f[i-1][j-1]
                    else:
                        f[i][j] = 0
                else:
                    if s[i] != p[j-1] and p[j-1] != ".":
                        f[i][j] = f[i][j-2]
                    else:
                        f[i][j] = f[i][j-2] or f[i-1][j]
        if f[len_s-1][len_p-1] == 1:
            return True
        else:
            return False

test = Solution()
print(test.isMatch("","."))


