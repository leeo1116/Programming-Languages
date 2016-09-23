class SVNRepo:
   @classmethod
   def isBadVersion(cls, id):
       pass
       # Run unit tests to check whether verison `id` is a bad version
       # return true if unit tests passed else false.
       # You can use SVNRepo.isBadVersion(10) to check whether version 10 is a
       # bad version.
class Solution:
    """
    @param n: An integers.
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # write your code here
        left, right = 1, n
        while left < right:
            mid = left+(right-left)//2
            if SVNRepo.isBadVersion(mid):
                right = mid
            else:
                left = mid+1
        return left