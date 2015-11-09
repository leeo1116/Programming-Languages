__doc__ = """
Given a string, find the length of the longest substring without repeating characters. For example, the
longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest
substring is "b", with the length of 1.
"""


class Solution(object):
    def __init__(self):
        pass

    def longest_non_repeating_substring(self, s):
        """
        Return the length of longest substring with no identical characters
        :param s: input string
        :return sub_s_len: max length of substring
        """
        str_dict = {}
        sub_s_len = 0
        # i1 -- start index of substring
        # i2 -- end index of substring
        i1 = 0
        for i2, char in enumerate(s):
            if str_dict.get(char, None) is not None:
                i1 = max(i1, str_dict[char]+1)
            str_dict[char] = i2
            sub_s_len = max(sub_s_len, i2-i1+1)
        return sub_s_len

s = Solution()
print(s.longest_non_repeating_substring('abba'))