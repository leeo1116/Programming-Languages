__doc__ = """
Write a function to find the longest common prefix string amongst an array of strings.
"""


class Solution(object):
    def __init__(self, index):
        self.index = index

    def longest_common_prefix(self, strs):
        """
        Return the longest common prefix of a list of strings
        :param strs:
        :return:
        """
        if len(strs) < 1:
            return ''
        # Find min length of the strings
        min_str_len = len(strs[0])
        for s in strs:
            if not s:
                return ''
            if len(s) < min_str_len:
                min_str_len = len(s)

        for i in range(min_str_len):
            char = strs[0][i]
            for s in strs:
                if s[i] != char:
                    return strs[0][:i]
        return strs[0][:i+1]


s = Solution(14)
print(s.longest_common_prefix(["a"]))