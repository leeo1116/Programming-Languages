__author__ = 'Liang Li'
class Solution:
    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):
        str_len = len(s)
        valid_IP = []
        i = 0
        while i < 3 and i < str_len-3:
            j = i+1
            while j <= i+3 and j < str_len-2:
                k = j+1
                while k <= j+3 and k < str_len-1:
                    s1 = s[:i+1]
                    s2 = s[i+1:j+1]
                    s3 = s[j+1:k+1]
                    s4 = s[k+1:]
                    if self.is_valid(s1) and self.is_valid(s2) \
                        and self.is_valid(s3) and self.is_valid(s4):
                        valid_IP.append(s1+'.'+s2+'.'+s3+'.'+s4)
                    k += 1
                j += 1
            i += 1
        return valid_IP

    def is_valid(self, s):
        valid = True
        s_len = len(s)
        if s_len < 1 or s_len > 3 or (s[0] == '0' and s_len > 1) or int(s) > 255:
            valid = False
        return valid

s = Solution()
print(s.restoreIpAddresses("010010"))
