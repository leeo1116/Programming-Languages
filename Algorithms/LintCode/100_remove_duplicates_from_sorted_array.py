class Solution(object):
    def remove_duplicates(self, A):
        if not A:
            return 0
        j = 1
        for i in range(1, len(A)):
            if A[i] != A[j-1]:
                A[j] = A[i]
                j += 1
        return j

s = Solution()
print(s.remove_duplicates([-10,0,1,2,3]))