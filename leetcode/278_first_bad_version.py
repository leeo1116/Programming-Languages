# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.first_bad_version(1, n)

    def first_bad_version(self, start, stop):
        if start == stop and isBadVersion(start):
            return start
        mid = start+(stop-start)//2
        if isBadVersion(mid):
            return self.firstBadVersion(start, mid)
        else:
            return self.firstBadVersion(mid+1, stop)
