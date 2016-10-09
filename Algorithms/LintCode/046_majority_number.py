class Solution(object):
    def majority_num(self, nums):
        major_num, count = 0, 0
        for num in nums:
            if num == major_num:
                count += 1
            elif count == 0:
                major_num = num
                count = 1
            else:
                count -= 1
        return major_num

s = Solution()
print(s.majority_num([1, 2, 1, 3, 4, 1, 1, 1, 1, 1]))