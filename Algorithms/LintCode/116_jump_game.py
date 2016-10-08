class Solution(object):
    def can_jump(self, A):
        i, max_index = 0, 0
        while i <= max_index:
            if max_index >= len(A)-1:
                return True
            max_index = max(A[i]+i, max_index)
            i += 1
        return False

s = Solution()
print(s.can_jump([2, 0, 1, 1, 3]))