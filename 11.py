from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n-1
        res = 0
        while i != j:
            if height[i] <= height[j]:
                s = height[i]*(j-i)
                i +=1
            else:
                s = height[j]*(j-i)
                j -=1
            if s > res:
                res = s
        return res

test = Solution()
print(test.maxArea([1,8,6,2,5,4,8,3,7]))