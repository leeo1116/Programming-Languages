class Solution(object):
    def search_matrix(self, matrix, target):
        if not matrix:
            return False
        row, col = len(matrix), len(matrix[0])
        left, right = 0, row*col-1
        while left <= right:
            mid = left+(right-left)//2
            if matrix[mid//col][mid%col] == target:
                return True
            elif matrix[mid//col][mid%col] > target:
                right = mid-1
            else:
                left = mid+1
        return False

s = Solution()
print(s.search_matrix([], 0))