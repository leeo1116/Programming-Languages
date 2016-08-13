class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.sums = [0]*len(nums)

        for i, num in enumerate(1, nums):
            if i == 0:
                self.sums[i] = nums[i]
            else:
                self.sums[i] = self.sums[i-1]+num

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j]-self.sums[i]+self.nums[i]



        # Your NumArray object will be instantiated and called as such:
        # numArray = NumArray(nums)
        # numArray.sumRange(0, 1)
        # numArray.sumRange(1, 2)