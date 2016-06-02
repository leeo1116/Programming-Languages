class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.stack.append([x, x])
        else:
            if x < self.stack[-1][1]:
                self.stack.append([x, x])
            else:
                self.stack.append([x, self.stack[-1][1]])

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]



# Your MinStack object will be instantiated and called as such:
s = MinStack()
s.push(3)
s.push(1)
s.push(2)
s.push(0)
print(s.top())
print(s.getMin())
s.pop()
print(s.getMin())
print(s.top())
