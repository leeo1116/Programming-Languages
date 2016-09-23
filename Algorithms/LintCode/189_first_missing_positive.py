class Solution(object):
    def first_missing_positive_map(self, A):
        number_flag = [False]*len(A)
        for i in range(len(A)):
            if len(A) >= A[i] > 0:
                number_flag[A[i]-1] = True
        for j in range(len(A)):
            if not number_flag[j]:
                return j+1
        return len(A)+1

    def first_missing_positive_replacement(self, A):
        for i in range(len(A)):
            while 0 < A[i] <= len(A) and A[i] != i+1 and A[i] != A[A[i]-1]:
                tmp = A[i]
                A[i] = A[A[i]-1]
                A[tmp-1] = tmp
        for j in range(len(A)):
            if A[j] != j+1:
                return j+1
        return len(A)+1

s = Solution()
print(s.first_missing_positive_replacement([3,4,-1,1]))
