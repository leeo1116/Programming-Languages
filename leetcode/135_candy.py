__author__ = 'Liang Li'
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candy = [1]*len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1]+1

        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1] and candy[i] <= candy[i+1]:
                candy[i] = candy[i+1]+1

        return sum(candy)
s = Solution()
print(s.candy([0]))

