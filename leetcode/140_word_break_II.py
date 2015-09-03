__author__ = 'liangl2'


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        if not s:
            return []
        valid_word = []
        valid_words = []
        for i in range(len(s)):
            for word in wordDict:
                if word == s[:i+1]:
                    valid_word = [word]+self.wordBreak(s[i+1:], wordDict)

            valid_words += valid_word
            return valid_words

s = Solution()
print(s.wordBreak("catsanddoge", ["cat", "cats", "and", "sand", "dog"]))

