class Solution(object):
    def longest_common_prefix(self, strs):
        """
        Find longest prefix of a list of strings
        :param strs: string list
        :return: longest common prefix
        """
        if not strs:
            return 0
        i, max_len, prefix = 0, 0, []
        while i < len(strs[0]):
            c = strs[0][i]
            for s in strs:
                if not s or i > len(s) or s[i] != c:
                    return prefix
            prefix.append(c)
            i += 1
        return prefix


s = Solution()
print(s.longest_common_prefix(["ABCD","DB","ABCEF"]))