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
            return self.LRU[key]
        else:
            return -1


    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if self.usage == self.capacity:
