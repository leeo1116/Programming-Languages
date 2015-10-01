__author__ = 'liangl2'
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_dict = {}
        for char in t:
            t_dict[char] = []
        miss = list(t)
        start = 0
        end = len(s)
        for i in range(len(s)):
            if s[i] not in miss and t_dict[s[i]] != []:
                t_dict[s[i]].pop(0)
            elif s[i] in miss:
                miss.remove(s[i])
            t_dict[s[i]].append(i)


