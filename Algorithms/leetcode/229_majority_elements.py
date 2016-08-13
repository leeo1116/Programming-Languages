class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return nums
        num_freq_dict = {}
        major_ele = []
        for n in nums:
            if num_freq_dict.get(n, 0) > len(nums)//3:
                continue
            num_freq_dict[n] = num_freq_dict.get(n, 0)+1
            if num_freq_dict[n] > len(nums)//3:
                major_ele.append(n)
        return major_ele

    def majority_element(self, nums):
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1

        c1, c2 = 0, 0
        major_ele = []
        for num in nums:
            if num == candidate1:
                c1 += 1
            if num == candidate2:
                c2 += 1
        if c1 > len(nums)//3:
            major_ele.append(candidate1)
        if c2 > len(nums)//3:
            major_ele.append(candidate2)
        return major_ele