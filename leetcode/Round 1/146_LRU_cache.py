__author__ = 'liangl2'
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.usage = 0
        self.LRU = {}
        self.usage_history = []

    def get(self, key):
        """
        :rtype: int
        """
        if self.LRU.get(key, None):
            self.usage_history.remove(key)
            self.usage_history.append(key)
            return self.LRU[key]
        else:
            return -1


    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key not in self.LRU: # Method 2, if self.get(key) == -1:
            if self.usage == self.capacity:
                self.LRU.pop(self.usage_history.pop(0))
                self.usage -= 1
            self.LRU[key] = value
            self.usage += 1
            self.usage_history.append(key)
        else:
            self.LRU[key] = value
            self.usage_history.remove(key)  # delete this line if using method 2
            self.usage_history.append(key)  # delete this line if using method 2

s = LRUCache(10)
