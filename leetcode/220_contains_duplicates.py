class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """ Naive brute-force method, got TLE
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        for i in range(len(nums)):
            j = i+1
            while j < len(nums) and j <= i+k:
                if abs(nums[i]-nums[j]) <= t:
                    return True
                j += 1
        return False
