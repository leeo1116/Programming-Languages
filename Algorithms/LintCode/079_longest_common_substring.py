class Solution:
    def longest_common_substring(self, A, B):
        """
        Find the longest common substring, return the length of it
        :param A: string A
        :param B: string B
        :return:  length of substring
        """
        m, n, max_len = len(A), len(B), 0
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if A[i] == B[j]:
                    dp[i][j] = dp[i-1][j-1]+1 if i > 0 and j > 0 else 1
                    max_len = max(max_len, dp[i][j])
        return max_len


s = Solution()
print(s.longest_common_substring("", ""))
