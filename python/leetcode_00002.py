# **********
# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例 1：
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 80
#
# 示例 2：
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#
# 示例 3：
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]
#
# 提示：
# 每个链表中的节点数在范围 [1, 100] 内
# 0 <= Node.val <= 9
# 题目数据保证列表表示的数字不含前导零
# **********

def add_two_numbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    l1_len = len(l1)
    l2_len = len(l2)

    result = l1
    result_len = l1_len
    other = l2
    other_len = l2_len
    if l1_len < l2_len:
        result = l2
        result_len = l2_len
        other = l1
        other_len = l1_len

    other += [0] * (result_len - other_len)

    tmp = 0
    for i in range(result_len):
        result[i] += other[i] + tmp
        if result[i] >= 10:
            tmp = result[i] // 10
            result[i] %= 10
        else:
            tmp = 0

    if tmp > 0:
        result.append(tmp)

    return result


assert add_two_numbers([2, 4, 3], [5, 6, 4]) == [7, 0, 8]

assert add_two_numbers([0], [0]) == [0]

assert add_two_numbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]) == [8, 9, 9, 9, 0, 0, 0, 1]


###################################################
class ListNode:

    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_


def list_node_to_array(node_list):
    result = []
    while node_list is not None:
        result.append(node_list.val)
        node_list = node_list.next
    return result


# leetcode　提交代码
class Solution:

    def addTwoNumbers(self, l1, l2):
        result = l1
        result_tail = l1

        tmp_node = ListNode(0)
        zero_node = ListNode(0)
        while l1 is not None:
            result_tail = l1
            l1.val += l2.val + tmp_node.val

            if l1.val >= 10:
                tmp_node.val = l1.val // 10
                l1.val %= 10
            else:
                tmp_node.val = 0

            if l1.next is None:
                l1 = l2.next
                l2 = tmp_node
            else:
                l1 = l1.next
                l2 = l2.next
                if l2 is None:
                    l2 = zero_node

        if tmp_node.val > 0:
            result_tail.next = tmp_node

        return result


solution = Solution()

l11 = ListNode(2, ListNode(4, ListNode(3)))
l12 = ListNode(5, ListNode(6, ListNode(4)))
sum1 = solution.addTwoNumbers(l11, l12)
result1 = list_node_to_array(sum1)
assert result1 == [7, 0, 8]

l21 = ListNode(0)
l22 = ListNode(0)
sum2 = solution.addTwoNumbers(l21, l22)
result2 = list_node_to_array(sum2)
assert result2 == [0]

l31 = ListNode(9, ListNode(9))
l32 = ListNode(9)
sum3 = solution.addTwoNumbers(l31, l32)
result3 = list_node_to_array(sum3)
assert result3 == [8, 0, 1]

l41 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l42 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
sum4 = solution.addTwoNumbers(l41, l42)
result4 = list_node_to_array(sum4)
assert result4 == [8, 9, 9, 9, 0, 0, 0, 1]
