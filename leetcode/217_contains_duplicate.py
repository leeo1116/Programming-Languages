class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_freq_dict = {}
        for num in nums:
            num_freq_dict[num] = num_freq_dict.get(num, 0)+1
            if num_freq_dict[num] >= 2:
                return True
        return False