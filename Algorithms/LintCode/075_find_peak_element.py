class Solution(object):
    def find_peak_traversal(self, A):
        for i in range(len(A)):
            if A[i] < A[i-1]:
                return i-1

    def find_peak_binary_search(self, A):
        left, right = 0, len(A)-1
        while left < right:
            mid1 = left+(right-left)//2
            mid2 = mid1+1
            if A[mid1] < A[mid2]:
                left = mid2
            else:
                right = mid1
        return left
