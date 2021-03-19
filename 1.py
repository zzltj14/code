from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    b = sorted(enumerate(nums), key=lambda x: x[1])
    maxCut = n
    for i in range(0, n):
        x = nums[b[i][0]]
        for j in range(i+1, maxCut):
            y = nums[b[j][0]]
            if x+y == target:
                return sorted([b[i][0], b[j][0]])
                break
            if x+y > target:
                maxCut = j
                break
    return [-1, -1]

print(twoSum([11, 7, 2, 15], 9))


# 参考答案------------------
# def twoSum(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     map_a = dict()
#     k = len(nums)
#     for i in range(0, k):  # 一边将列表中的数添加到字典中，一边判断两数之差是否存在于字典中
#         temp = target - nums[i]
#         if temp in map_a:  # 判断步骤
#             return [map_a[temp], i]
#         map_a[nums[i]] = i  # 添加步骤（切记先判断再添加，以免key冲突）
#
# print(twoSum([11, 7, 2, 15], 9))