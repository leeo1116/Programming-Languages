class Solution(object):
    def merge_two_sorted_arrays(self, A, B):
        C = [0]*(len(A)+len(B))
        j, k = 0, 0
        for i in range(len(C)):
            if j < len(A) and k < len(B) and A[j] < B[k]:
                C[i] = A[j]
                j += 1
            elif j < len(A) and k < len(B) and A[j] >= B[k]:
                C[i] = B[k]
                k += 1
            elif k >= len(B):
                C[i] = A[j]
                j += 1
            elif j >= len(A):
                C[i] = B[k]
                k += 1
        return C