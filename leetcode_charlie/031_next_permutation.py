class Solution(object):
    def next_permutation(self, nums):
        """
        Step1 - From right to left, find the first digit that is smaller than its right side one. Call it violation_num
        Step2 - From right to left, find the first digit that is greater than violation_num. Call it change_num
        Step3 - Swap violation_num and change_num
        Step4 - Reverse digits from right to original violation_num

        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        violation_num, change_num = -1, -1
        # from right to left, find first digit that is smaller than its right side one
        for i in range(len(nums)-1, -1, -1):
            if i and nums[i-1] < nums[i]:
                violation_num = nums[i-1]
                violation_index = i-1
                break

        # from right to left, find the first digit that is greater than violation_num
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > violation_num:
                change_num = nums[i]
                change_index = i
                break

        if violation_num != -1: # and change_num != -1:
            # swap violation_num and change_num
            nums[violation_index], nums[change_index] = nums[change_index], nums[violation_index]

            # reverse from right to original violation_num
            nums[violation_index+1:] = nums[:violation_index:-1]
        else:
            nums[::] = nums[::-1]


s = Solution()
a = [3, 2, 1]
s.next_permutation(a)
print(a)

