__author__ = 'Liang Li'
class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        haystack_len = len(haystack)
        needle_len = len(needle)
        if not needle:
            return 0
        if needle_len > haystack_len or not haystack:
            return -1

        for i in range(haystack_len):
            for j in range(needle_len):
                if i+j >= haystack_len:
                    return -1
                if haystack[i+j] != needle[j]:
                    break
            if j == needle_len-1 and needle[j] == haystack[i+j]:
                return i
        return -1


s = Solution()
print(s.strStr("mississippi", "issip"))
