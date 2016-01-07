__doc__  = """Implement strStr(). Returns the index of the first occurrence of needle in haystack, or -1 if needle is
 not part of haystack."""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        h_len = len(haystack)
        n_len = len(needle)
        if not h_len or not n_len:
            return 0 if (h_len == n_len or not n_len) else -1

        for i in range(h_len):
            j = 0
            for j in range(n_len):
                if i+j >= h_len:
                    return -1
                if haystack[i+j] != needle[j]:
                    break
            if j == n_len-1 and needle[j] == haystack[i+j]:
                return i
        return -1






