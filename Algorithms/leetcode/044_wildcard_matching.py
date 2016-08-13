__author__ = 'Liang Li'
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i, j = 0, 0
        match_index = 0
        star_index = -1
        while i < len(s):
            if j < len(p) and (p[j] == '?' or s[i] == p[j]):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                star_index = j
                match_index = i
                j += 1
            elif star_index != -1:
                j = star_index+1
                match_index += 1
                i = match_index
            else:
                return False
        while j < len(p) and p[j] == '*':
            j += 1
        return j == len(p)

class Solution(object):
    def is_match_dp(self, s, p):
        str_len = len(s)
        if len(p)-p.count('*') > str_len:
            return False
        dp = [True]+[False]*str_len
        for p_c in p:
            if p_c != '*':
                for str_index in reversed(range(str_len)):
                    dp[str_index+1] = dp[str_index] and (p_c == s[str_index] or p_c == '?')
            else:
                for str_index in range(1, str_len+1):
                    dp[str_index] = dp[str_index-1] or dp[str_index]
            dp[0] = dp[0] and p_c == '*'
        return dp[-1]
s = Solution()
print(s.isMatch("liangli", "*"))