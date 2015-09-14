__author__ = 'liangl2'
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        self.dict = wordDict
        self.cache = {}
        return self.break_helper(s)

    def break_helper(self, s):
        combs = []
        if s in self.cache:
            return self.cache[s]
        if len(s) == 0:
            return []

        for i in range(len(s)):
            if s[:i+1] in self.dict:
                if i == len(s) - 1:
                    combs.append(s[:i+1])
                else:
                    sub_combs = self.break_helper(s[i+1:])
                    for sub_comb in sub_combs:
                        combs.append(s[:i+1] + ' ' + sub_comb)

        self.cache[s] = combs
        return combs

s = Solution()
print(s.wordBreak("aaaaaaa", ["aaaa","aaa"]))

