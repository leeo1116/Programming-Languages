class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        count = [0]*(num+1)
        j = 0

        for i in range(1, num+1):
            k = i & (2**j-1)
            if i == 2**(j+1)-1:
                j += 1
            count[i] = count[k] + 1
        return count


s = Solution()
print(s.countBits(3))
