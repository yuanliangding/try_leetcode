# **********
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
# 示例 2:
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
# 示例 3:
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
# 提示：
# 0 <= s.length <= 5 * 104
# s 由英文字母、数字、符号和空格组成
# **********

def length_of_longest_substring(s):
    """
    :type s: str
    :rtype: int
    """
    result, result_pos_begin, result_pos_end = 0, 0, 0

    for ch in s:
        hit_pos = s.find(ch, result_pos_begin, result_pos_end)
        if -1 != hit_pos:
            result = max(result, result_pos_end - result_pos_begin)
            result_pos_begin = hit_pos + 1

        result_pos_end += 1

    return max(result, result_pos_end - result_pos_begin)


assert length_of_longest_substring("abcabcbb") == 3
assert length_of_longest_substring("bbbbb") == 1
assert length_of_longest_substring("pwwkew") == 3
assert length_of_longest_substring("abba") == 2


###################################################
# leetcode　提交代码
class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, result_pos_begin, result_pos_end = 0, 0, 0

        for ch in s:
            hit_pos = s.find(ch, result_pos_begin, result_pos_end)
            if -1 != hit_pos:
                result = max(result, result_pos_end - result_pos_begin)
                result_pos_begin = hit_pos + 1

            result_pos_end += 1

        return max(result, result_pos_end - result_pos_begin)


solution = Solution()

assert solution.lengthOfLongestSubstring("abcabcbb") == 3
assert solution.lengthOfLongestSubstring("bbbbb") == 1
assert solution.lengthOfLongestSubstring("pwwkew") == 3
assert solution.lengthOfLongestSubstring("abba") == 2
