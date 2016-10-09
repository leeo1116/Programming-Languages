class Solution(object):
    def single_number_II(self, A):
        B1, B0 = 0, 0
        for a in A:
            B1_tmp = B1
            B1 = (~a) & B1 & (~B0) | a & (~B1) & (B0)
            B0 = (~B1_tmp) & (a ^ B0)
        return B0

s = Solution()
print(s.single_number_II([1,1,2,3,3,3,2,2,4,1]))
