import random
__doc__ = """
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of
their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""


class ListNode(object):
    def __init__(self, value):
        self.val = value
        self.next = None


class Solution(object):
    def __init__(self, index):
        self.index = index

    def add_two_numbers(self, l1, l2):
        print('#{0} Solution:\n'.format(self.index))
        carry_in = 0
        l3 = dummy_head = ListNode(0)
        while l1 or l2 or carry_in:
            # Get each digit and add them up with carry_in
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            digit_sum = (digit1+digit2+carry_in) % 10
            carry_in = (digit1+digit2+carry_in) // 10
            # Create a ListNode object with val = digit_sum, link it to l3
            l3.next = ListNode(digit_sum)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            l3 = l3.next
        return dummy_head.next


def rand_list(n, low, high):
    """
    Generate rand integer list
    :param n: list length
    :param low: lower bound
    :param high: higher bound
    :return head.next: head of the list
    """
    h = head = ListNode(0)
    while n:
        h.next = ListNode(random.randint(low, high))
        h = h.next
        n -= 1
    return head.next


def print_list(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    return None

s = Solution(index=2)
l1 = rand_list(3, 5, 9)
l2 = rand_list(2, 6, 9)
print_list(l1)
print('')
print_list(l2)
print('')
new_head = s.add_two_numbers(l1, l2)
print_list(new_head)