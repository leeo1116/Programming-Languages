import collections


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_freq_dict1 = {}
        char_freq_dict2 = {}
        for i in range(len(s)):
            if char_freq_dict1.get(s[i], None) != char_freq_dict2.get(t[i], None):
                return False
            char_freq_dict1[s[i]] = i
            char_freq_dict2[t[i]] = i
        return True
