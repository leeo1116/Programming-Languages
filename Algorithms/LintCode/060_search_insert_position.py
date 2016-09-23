class Solution(object):
    def search_insert_position(self, A, target):
        left, right = 0, len(A)-1
        while left <= right:
            mid = left+(right-left)//2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return left

s = Solution()
print(s.search_insert_position([10, 12], 9))