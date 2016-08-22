class Solution(object):
    def remove_element(self, A, elem):
        """
        Remove occurrences of elem in A in place and return new length
        :param A: array A
        :param elem: target element
        :return: new length
        """
        j = 0
        for i in range(len(A)):
            if A[i] != elem:
                A[j] = A[i]
                j += 1
        return j

s = Solution()
print(s.remove_element([1, 2, 3, 0], 0))