"""
字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑
eg: 
输入: 
first = "pale"
second = "ple"
输出: True
eg2:
输入: 
first = "pales"
second = "pal"
输出: False
思路：
self
字符串一次只能有一个操作，插入、删除、替换
可以根据两个字符串长度来判断是哪个操作
better:
固定长短（类似）
比较字符（类似）
比较后面（决定）（因为确定了长度，所以可以直接取不同地方的后面字符串比较即可）
增删改功能特点就是：自不同位起，后续都一样
"""
def oneEditAway(first, second):
    """
        :type first: str
        :type second: str
        :rtype: bool
    """
    if first == second:
        return True
    if abs(len(first) - len(second)) > 1:
        return False
    if len(first) >= len(second):
        # 调整为前小后大的排序
        first, second = second, first
    for index, i in enumerate(second):
        if len(first) >= index + 1 and first[index] != second[index]:
            temp = list(first)
            temp.insert(index, i)
            temp_rep = list(first)
            temp_rep[index] = i
            if (''.join(temp) != second and len(first) != len(second)) or (''.join(temp_rep) != second and len(first) == len(second)):
                return False
            else:
                return True
        elif len(first) < index + 1:
            # 超出较短字符串长度
            temp = list(first)
            temp.append(i)
            if ''.join(temp) != second:
                return False
            else:
                return True

def oneEditAway_better(first: str, second: str) -> bool:
    # -> 常常出现在函数定义的函数名后面，为函数添加元数据,描述函数的返回类型，从而方便开发人员使用
    if abs(len(second) - len(first)) > 1: return False
    if len(second) - len(first) < 0:
        first, second = second, first
    for i in range(len(first)):
        if first[i] == second[i]:
            continue
        # 遇到不一样了，可能：增；改
        return first[i:] == second[i + 1:] or first[i+1:] == second[i+1:]
    return True

# first = input('请输入第一个数： ')
# second = input("请输入第二个数: ")
# print(oneEditAway(first, second))
# print(oneEditAway_better(first=first, second=second))

"""
字符串压缩(如果要压缩，长度必须小于原字符串)
'aaaa' -> 'a4'
'aabb' -> 'aabb'
'aabbbb' -> 'a2b4'
better:思路
使用min() 以及 itertools的groupby方法
gruopby方法可以分组
eg: 
    'aaabbbbbbccc'
    分组后
    a, 'aaa'
    b, 'bbbbbb'
    c, 'ccc'
"""
import itertools
def compressString_better(s):
    min(s, ''.join(k + str(len(list(v))) for k, v in itertools.groupby(s)), key=len)


def twoSum(nums, target: int):
    for i_index, i in enumerate(nums):
        if i >= target:
            continue
        x = target - i
        try:
            x_index = nums.index(x, i_index+1)
        except Exception as e:
            x_index = -2
        if x in nums and x_index != -2 and i_index != x_index:
            return [nums.index(i), nums.index(x)]

# first = input('请输入：')
# sum = int(input("和： "))
# first = [int(i) for i in list(first)]
# print(first)
# print(twoSum(first, sum))


def addTwoNumbers(l1, l2):
    if len(l1) > len(l2):
        # 保证长度顺序
        l1, l2 = l2, l1
    temp_bit = 0
    last_list = []
    for i in range(len(l1)):
        sum = (l1[i] + l2[i] + temp_bit) % 10
        temp_bit = (l1[i] + l2[i]) // 10
        last_list.append(sum)
    temp_bit and last_list.append(temp_bit)
    return last_list

# first = eval(input('请输入：'))
# second = eval(input('请输入： '))
# print(addTwoNumbers(first, second))


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sumNode = ListNode(0)
        return self.add_numbers(l1, l2, sumNode)
    def add_numbers(self, l1: ListNode, l2: ListNode, sumNode: ListNode, bit=0) -> ListNode:
        l1_value = (hasattr(l1,'val') and l1.val) or 0
        l2_value = (hasattr(l2,'val') and l2.val) or 0
        sumNode.val = (l1_value + l2_value + bit) % 10
        bit = (l1_value + l2_value + bit) // 10
        if (hasattr(l1,'next') and l1.next) or (hasattr(l2,'next') and l2.next) or bit:
            # 存在下游节点或者有进位
            sumNode.next = self.add_numbers((hasattr(l1,'next') and l1.next) or None, (hasattr(l2,'next') and l2.next) or None, ListNode(0), bit)
        elif not bit:
            sumNode.next = None
        return sumNode

if __name__ == '__main__':
    x = ListNode(2, ListNode(4, ListNode(3, None)))
    y = ListNode(5, ListNode(6, ListNode(4, None)))
    x9 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))
    y9 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, None)))))))
    result = Solution()
    z = result.addTwoNumbers(x, y)
    z9 = result.addTwoNumbers(x9, y9)
    print(z)