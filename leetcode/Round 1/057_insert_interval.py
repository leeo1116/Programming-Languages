__author__ = 'liangl2'
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        inserted_interval = []
        i = 0
        start, end = newInterval.start, newInterval.end
        while i < len(intervals):
            if newInterval.start <= intervals[i].end:
                if newInterval.end < intervals[i].start:
                    break
                start = min(newInterval.start, intervals[i].start, start)
                end = max(newInterval.end, intervals[i].end, end)
            else:
                inserted_interval.append(intervals[i])
            i += 1
        inserted_interval.append(Interval(start, end))
        inserted_interval += intervals[i:]
        return inserted_interval

