class Solution(object):
    def remove_duplicates(self, A):
        if not A:
            return 0
        j = 0
        for i in range(len(A)):
            if i == 0:
                count = 1
                j += 1
            else:
                if A[i] != A[i-1] or count < 2:
                    if A[i] != A[i-1]:
                        count = 1
                    else:
                        count += 1
                    A[j] = A[i]
                    j += 1
        return j

s = Solution()
print(s.remove_duplicates([-1014,-1014,-1014,-999,-999,-998]))