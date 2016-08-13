class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_index_dict = {}
        for i, num in enumerate(nums):
            if num_index_dict.get(num, None) != None:
                if i - num_index_dict[num] <= k:
                    return True
            num_index_dict[num] = i
        return False

s = Solution()
print(s.containsNearbyDuplicate([1, 0, 1, 1], 1))