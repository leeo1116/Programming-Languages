__author__ = 'Liang Li'
class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if not strs or '' in strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        min_str_len = len(strs[0])
        for str in strs:
            min_str_len = len(str) if len(str) < min_str_len else min_str_len
        for i in range(min_str_len):
            tmp = strs[0][i]
            for str in strs:
                if str[i] != tmp:
                    return strs[0][:i]
        return strs[0][:min_str_len]


s = Solution()
print(s.longestCommonPrefix(["cc", "c"]))
