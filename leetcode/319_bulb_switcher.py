import math

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))
        # bulb_status_list = [1]*n
        # bulbs_on = 0
        # for i in range(2, n+1):
        #     for j in range(i, n+1):
        #         if j % i == 0:
        #             bulb_status_list[j-1] = 1 if bulb_status_list[j-1] == 0 else 0
        #
        # for k in range(n):
        #     if bulb_status_list[k]:
        #         bulbs_on += 1
        #
        # return bulbs_on


s = Solution()
print(s.bulbSwitch(9999))