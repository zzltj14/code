import numpy as np


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        curr_delta = 0
        i_save = 0
        j_save = 0
        table = np.zeros((n, n))
        for i in range(n):
            j = i
            table[i, j] = 1
        for delta in [1, 2]:
            i = 0
            j = i + delta
            while j <= n - 1:
                if s[i] == s[j]:
                    table[i, j] = 1
                    if delta > curr_delta:
                        curr_delta = delta
                        i_save = i
                        j_save = j
                i = i + 1
                j = j + 1
        for delta in range(3, n):
            i = 0
            j = i + delta
            while j <= n - 1:
                if s[i] == s[j] and table[i+1, j-1] == 1:
                    table[i, j] = 1
                    if delta > curr_delta:
                        curr_delta = delta
                        i_save = i
                        j_save = j
                i = i + 1
                j = j + 1
        return (s[i_save:j_save+1])

test = Solution()
print(test.longestPalindrome("cbbd"))
