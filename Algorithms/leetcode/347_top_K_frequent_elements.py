class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        num_freq_dict = {}
        bucket_list = [[] for i in range(len(nums))]
        most_k_freq_list = []
        for num in nums:
            num_freq_dict[num] = num_freq_dict.get(num, 0)+1

        for num_key, freq_value in num_freq_dict.items():
            bucket_list[freq_value-1].append(num_key)

        for i in range(len(bucket_list)-1, -1, -1):
            if len(most_k_freq_list) == k:
                break
            if bucket_list[i]:
                most_k_freq_list += bucket_list[i]

        return most_k_freq_list


s = Solution()
print(s.topKFrequent([1, 1, 1, 2, 3, 3, 3, 3, 4, 4, 6, 8], 3))

