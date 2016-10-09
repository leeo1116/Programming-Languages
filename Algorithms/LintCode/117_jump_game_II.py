class Solution(object):
    def jump(self, A):
        """
        Find minimum steps to jump from first element to last element in A
        :param A: list of elements
        :type A: list
        :return: minimum steps to reach the end
        :rtype: int
        """
        # write your code here
        if len(A) < 2:
            return 0
        i = max_end = max_one_step_end = min_steps = 0
        for i in range(len(A)):
            max_end = max(max_end, i + A[i])
            if max_end >= len(A) - 1:
                return min_steps + 1
            if i == max_one_step_end:
                max_one_step_end = max_end
                min_steps += 1

s = Solution()
print(s.jump([2, 8, 2, 1, 2, 1, 2, 1, 1, 2, 1]))