class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        # write your code here
        left, right = 0, len(A)-1
        while left <= right:
            mid = left+(right-left)//2
            if A[mid] == target:
                return mid
            elif A[left] < A[mid] and A[left] <= target < A[mid] or A[left] > A[mid] and not (A[right] > target >= A[mid]):
                right = mid-1
            else:
                left = mid+1
        return -1
    