class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        sq_num = [n]*(n+1)
        sq_num[0] = 0
        for i in range(1, n+1):
            j = 1
            while j*j <= i:
                sq_num[i] = min(sq_num[i], sq_num[i-j*j]+1)
                j += 1
        return sq_num[n]

    def num_squares_bfs(self, n):
        if n < 2:
            return n
        lst, i = [], 1
        while i*i <= n:
            lst.append(i)
            i += 1

        count = 0
        square_res = set({n})
        while square_res:
            count += 1
            temp = set()
            for x in square_res:
                for y in lst:
                    if x == y:
                        return count
                    if x < y:
                        break
                    temp.add(x-y)
            square_res = temp

        return count

s = Solution()
print(s.numSquares(9975))