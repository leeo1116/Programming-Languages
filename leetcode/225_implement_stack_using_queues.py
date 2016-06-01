import collections


class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = collections.deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        queue_len = len(self.queue)
        while queue_len-1:
            self.quequ.append(self.queue.popleft())
            queue_len -= 1
        self.queue.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.queue[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.queue
