class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_freq_dict = {}
        for num in nums:
            num_freq_dict[num] = num_freq_dict.get(num, 0)+1
            if num_freq_dict[num] > len(nums)//2:
                return num_freq_dict[num]