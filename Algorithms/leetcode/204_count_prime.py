class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        is_prime_list = [False]*n
        for i in range(2, n):
            is_prime_list[i] = True

        j = 2
        while j*j < n:
            if not is_prime_list[j]:
                j += 1
                continue
            for k in range(j*j, n, j):
                is_prime_list[k] = False
            j += 1

        count = 0
        for is_prime in is_prime_list:
            if is_prime:
                count += 1

        return count



s = Solution()
print(s.countPrimes(2))