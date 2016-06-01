__author__ = 'liang li'


class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack1.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def peek(self):
        """
        :rtype: int
        """
        return self.stack1[0]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack1
