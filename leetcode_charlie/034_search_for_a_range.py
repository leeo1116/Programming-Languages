class Solution(object):
    def search_range(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # search for left index
        low, high = 0, len(nums)-1
        index = [-1, -1]
        while low < high:
            mid = low+(high-low)//2
            if target > nums[mid]:
                low = mid+1
            else:
                high = mid
        if nums[low] != target:
            return index
        else:
            index[0] = low

        # search for right index
        high = len(nums)-1
        while low < high:
            mid = low+(high-low)//2+1
            if nums[mid] > target:
                high = mid-1
            else:
                low = mid
        index[1] = high
        return index

