#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
# 本题中排序列表是关键判断条件所在
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tmp = 0
        for i in range(1,len(nums)):
            if nums[tmp] != nums[i]:
                tmp = tmp + 1
                nums[tmp] = nums[i]
        return tmp + 1
# @lc code=end

