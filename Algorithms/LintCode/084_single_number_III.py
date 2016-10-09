class Solution:
    def singleNumberIII(self, A):
        """
        Find two elements in A that only occur one time, all other elements occur exactly 2 times
        :param A: list of elements
        :return: two elements that occur one time
        :type A: list
        :rtype: list
        """
        xor_result, bit1_index = 0, 0
        for a in A:
            xor_result ^= a
        for i in range(32):
            if (xor_result >> i) & 1 == 1:
                bit1_index = i
        n1, n2 = 0, 0
        for j in range(len(A)):
            if A[j] & (1 << bit1_index) != 0:
                n1 ^= A[j]
            else:
                n2 ^= A[j]
        return [n1, n2]


s = Solution()
print(s.singleNumberIII([1,2,3,3,2,4,1,5]))

