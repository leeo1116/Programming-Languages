class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        line_num = len(x)
        if line_num < 4:
            return False

        for i in range(3, line_num):
            if x[i] >= x[i-2] and x[i-1] <= x[i-3]:
                return True
            if i >= 4:
                if x[i-1] == x[i-3] and x[i] + x[i-4] >= x[i-2]:
                    return True
            if i >= 5:
                if x[i] >= x[i-2] - x[i-4] >= 0 and x[i-3] - x[i-5] <= x[i-1] <= x[i-3]:
                    return True
        return False

    def is_self_crossing(self, x):
        line_num = len(x)
        if line_num < 4:
            return False

        if x[2] > x[0]:
            flag = 1  # diverging
        else:
            flag = 0  # converging

        for i in range(3, line_num):
            if flag == 0 and x[i] >= x[i-2]:
                return True
            if flag == 1 and x[i] <= x[i-2]:
                flag = 0
            if i >= 5 and flag == 0 and x[i]+x[i-4] >= x[i-2]:
                return True
        return False


s = Solution()
print(s.isSelfCrossing([2, 5, 4]))