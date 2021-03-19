from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        cur1 = 0
        cur2 = 0
        n = n1 + n2
        k1 = (n1 + n2 - 1) // 2
        k2 = (n1 + n2) // 2

        def findK(start1,  start2, k):
            len1 = n1 - start1
            len2 = n2 - start2
            mid1 = nums1[start1:]
            mid2 = nums2[start2:]
            index1 = min(len1-1, (k-1)//2)
            index2 = min(len2-1, (k-1)//2)
            if len1 < 1:
                return mid2[k]
            if len2 < 1:
                return mid1[k]
            if k == 0:
                return min(mid1[0], mid2[0])

            if mid1[index1] < mid2[index2]:
                return findK(start1 + index1 + 1, start2, k-index1-1)
            else:
                return findK(start1, start2 + index2 + 1, k-index2-1)

        return (findK(0, 0, k1)+findK(0, 0, k2))/2


test = Solution()
# print(test.findMedianSortedArrays([1, 2],[-1,3]))
# print(test.findMedianSortedArrays([1, 2],[3,4]))
print(test.findMedianSortedArrays([1],[2,3,4,5,6]))
