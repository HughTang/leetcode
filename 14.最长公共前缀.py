#
# @lc app=leetcode.cn id=14 lang=python
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        :zip()函数：用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，可以使用 list() 转换来输出列表。
        在python3中zip中的数据只能操作一次，内存就会释放，当下次访问时就会报错。python2中zip中的数据可以访问多次。
        :set()函数：创建一个无序不重复元素集，可进行关系测试，删除重复数据。
        """
        res = ""
        for tmp in list(zip(*strs)):
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                res += tmp[0]
            else:
                break
        return res
# @lc code=end