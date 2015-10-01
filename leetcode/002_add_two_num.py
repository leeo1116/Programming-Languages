__author__ = 'Liang Li'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def add_two_num(self, l1, l2):
        l3 = ListNode(0)
        while l1 or l2:
            tmp = l1.val+l2.val
            if tmp > 10:
                l3.val = tmp % 10
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next
        return l3

def integer2list(integer):
    digits = list(map(int, str(integer)))  # integer to list
    head = ListNode(0)
    for digit in digits:
        current_node = ListNode(digit)
        current_node.next = head.next  # List-Insert at head
        head.next = current_node
    return head

def integer2list_reverse(integer):
    digits = [int(digit) for digit in str(integer)]  # integer to list
    head = ListNode(0)
    tail = head
    for digit in digits:
        current_node = ListNode(digit)
        tail.next = current_node
        tail = current_node
    return head

def integer2list_x(integer):
    digits = [int(digit) for digit in str(integer)]  # integer to list
    head = ListNode(0)
    for digit in digits:
        current_node = ListNode(digit)
        current_node.next = head
        head = current_node
    return head

num1 = 2341
num2 = 19
l1 = integer2list_reverse(num1)
head = l1.next
while head:
    print(head.val, end='')
    head = head.next
print('')

l2 = integer2list_reverse(num1)
head = l2.next
while head:
    print(head.val, end='')
    head = head.next
print('')

l3 = integer2list_x(num1)
while l3.next:
    print(l3.val, end='')
    l3 = l3.next
