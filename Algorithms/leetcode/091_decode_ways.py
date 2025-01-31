__author__ = 'Liang Li'
class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        # dp[i] = dp[i-1] if s[i] != "0"
        #        +dp[i-2] if "09" < s[i-1:i+1] < "27"
        if s == "":
            return 0

        dp = [0]*(len(s)+1)
        dp[0] = 1
        for i in range(1, len(s)+1):
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            if i != 1 and "09" < s[i-2:i] < "27":  #"01"ways = 0
                dp[i] += dp[i-2]
        return dp[len(s)]

s = Solution()
print(s.numDecodings("1201"))