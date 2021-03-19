# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         n = len(s)
#         if n == 0:
#             return 0
#         cur = 1
#         for i in range(0,n):
#             cur_max = 1
#             for j in range(i+1,n):
#                 if s[j] in s[i:j]:
#                     break
#                 cur_max = cur_max + 1
#             cur = max(cur_max, cur)
#         return cur

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:max_len = cur_len
            lookup.add(s[i])
        return max_len


test = Solution()
print(test.lengthOfLongestSubstring(""))
