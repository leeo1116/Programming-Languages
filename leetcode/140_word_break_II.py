__author__ = 'liangl2'
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        word_dict = [False]*len(s)
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i-len(w)+1:i+1] and (word_dict[i-len(w)] or i-len(w) == -1):
                    word_dict[i] = True
        return word_dict[-1]