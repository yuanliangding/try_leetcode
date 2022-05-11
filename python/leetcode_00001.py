# **********
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 你可以按任意顺序返回答案。
#
# 示例 1：
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
#
# 示例 2：
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
#
# 示例 3：
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
#  
# 提示：
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# 只会存在一个有效答案
# 进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？
# **********

def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    result = []

    index = {}

    for pos in range(len(nums)):
        if target - nums[pos] in index.keys():
            result.append(index[target - nums[pos]])
            result.append(pos)
            break
        else:
            index[nums[pos]] = pos

    return result


assert two_sum([2, 7, 11, 15], 9) == [0, 1]

assert two_sum([3, 2, 4], 6) == [1, 2]

assert two_sum([3, 3], 6) == [0, 1]


###################################################
# leetcode　提交代码
class Solution:

    def twoSum(self, nums, target):
        index = {}
        for pos in range(len(nums)):
            if target - nums[pos] in index.keys():
                return [index[target - nums[pos]], pos]
            else:
                index[nums[pos]] = pos

        return []


solution = Solution()

assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
assert solution.twoSum([3, 2, 4], 6) == [1, 2]
assert solution.twoSum([3, 3], 6) == [0, 1]
