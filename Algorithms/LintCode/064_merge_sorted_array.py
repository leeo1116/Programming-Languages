class Solution(object):
    def merge_sorted_array(self, A, m, B, n):
        if not A or not B:
            return
        i, j = m - 1, n - 1
        for k in range(m + n - 1, -1, -1):
            if j >= 0 and i >= 0 and A[i] < B[j]:
                A[k] = B[j]
                j -= 1
            elif i >= 0 and j >= 0 and A[i] >= B[j]:
                A[k] = A[i]
                i -= 1
            elif i < 0:
                A[k] = B[j]
                j -= 1