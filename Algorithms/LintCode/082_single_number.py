class Solution(object):
    def single_number(self, A):
        single_num = 0
        for a in A:
            single_num ^= a
        return single_num

s = Solution()
print(s.single_number([2, 1, 2, 1, 3, 4, 4, 5, 5]))