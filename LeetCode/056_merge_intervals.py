__author__ = 'liangl2'
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        merged_list = []
        for i in (sorted(intervals, key=lambda i: i.start)):
            if merged_list and i.start <= merged_list[-1].end:
                merged_list[-1].end = max(merged_list[-1].end, i.end)
            else:
                merged_list += i,
        return merged_list
