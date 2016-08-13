"""
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of
substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
"""

class Solution(object):
    def find_substring(self, s, words):
        """
        find all indices of words concatenation in a string
        :type s: str
        :type words: list
        :param s: string that contains words
        :param words: words that have the same length
        :return: indices of all concatenation words in string s
        :rtype: list[int]
        """
        if len(words) == 0:
            return []
        word_len = len(words[0])
        index = []
        for i in range(len(s)):
            for j in range(len(words)):
                if s[j*word_len+i:j*word_len+i+word_len] not in words:
                    j = 0
                    break
            if j == len(words)-1:
                index.append(i)
        return index


s = Solution()
print(s.find_substring("barfoothefoobarman", ["foo", "bar"]))