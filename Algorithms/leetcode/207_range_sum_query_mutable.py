class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.num_array = nums
        self.pre_sum = [0]*len(nums)
        tmp = 0
        for i in range(len(nums)):
            tmp += nums[i]
            self.pre_sum[i] = tmp

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        for j in range(i, len(self.num_array)):
            self.pre_sum[j] += (val - self.num_array[i])

        self.num_array[i] = val
        return val

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.pre_sum[j]-self.pre_sum[i-1] if i else self.pre_sum[j]



# Your NumArray object will be instantiated and called as such:
nums = [1, 3, 5]
numArray = NumArray(nums)
print(numArray.sumRange(0, 2))
print(numArray.update(1, 2))
print(numArray.sumRange(0, 2))