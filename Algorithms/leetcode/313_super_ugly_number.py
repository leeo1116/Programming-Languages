class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly = [1] * n
        i_list = [-1]*len(primes)
        v_list = [1]*len(primes)
        k = 0
        while k < n:
            cur_ugly = min(v_list)
            ugly[k] = cur_ugly
            for v in range(len(v_list)):
                if cur_ugly == v_list[v]:
                    i_list[v] += 1
                    v_list[v] = ugly[i_list[v]]*primes[v]
            k += 1
        return ugly[k-1]



s = Solution()
print(s.nthSuperUglyNumber(8, [2, 3]))
