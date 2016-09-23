class Solution(object):
    def search_range(self, A, target):
        left, right = 0, len(A)-1
        target_range = [-1, -1]
        while left < right:
            mid = left+(right-left)//2
            if A[mid] < target:
                left = mid+1
            else:
                right = mid
        if A[left] != target:
            return target_range
        else:
            target_range[0] = left

        right = len(A)-1
        while left < right:
            mid = left+(right-left)//2+1
            if A[mid] > target:
                right = mid-1
            else:
                left = mid
        target_range[1] = right
        return target_range

s = Solution()
print(s.search_range([5, 7, 7, 8, 8, 10], 7))
