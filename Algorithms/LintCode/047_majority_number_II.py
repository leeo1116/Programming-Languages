class Solution(object):
    def majority_number_II(self, nums):
        candidate1 = candidate2 = count1 = count2 = 0
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 = 1
            elif count2 == 0:
                candidate2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        count1 = count2 = 0
        for n in nums:
            if n == candidate1:
                count1 += 1
            if n == candidate2:
                count2 += 1
        return candidate1 if count1 > count2 else candidate2
