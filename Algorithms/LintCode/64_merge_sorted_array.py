class Solution(object):
    def merge_sorted_array(self, A, m, B, n):
        i, j = m - 1, n - 1
        A = A+B
        for k in range(m + n - 1, -1, -1):
            if j >= 0 and A[i] < B[j]:
                A[k] = B[j]
                j -= 1
            elif i >= 0 and A[i] > B[j]:
                A[k] = A[i]
                i -= 1

s = Solution()
s.merge_sorted_array([1,3,4,6], 4, [2,5], 2)