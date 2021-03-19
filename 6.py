class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s)
        res = ["" for _ in range(numRows)]
        cur_row = 0
        flag = 1
        for i in range(n):
            res[cur_row] = res[cur_row] + s[i]
            cur_row = cur_row + flag
            if cur_row == 0 or cur_row == numRows-1:
                flag = -flag
        return "".join(res)


test = Solution()
print(test.convert("LEETCODEISHIRING",3))
