__author__ = 'Liang Li'
class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        lst = [col_element for row in matrix for col_element in row]
        low, high = 0, len(lst)-1
        while low <= high:
            mid = low+(high-low)//2
            if lst[mid] < target:
                low = mid+1
            elif lst[mid] > target:
                high = mid-1
            else:
                return True
        return False

s = Solution()
print(s.searchMatrix([[1, 2, 3], [4, 6, 8], [10, 13, 14]], 8))