class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        char_index_dict = {}
        for i, c in enumerate(s):
            if char_index_dict.get(c, None):
                char_index_dict[c].append(i)
            else:
                char_index_dict[c] = [i]

        unique_s = ""

        for i, c in enumerate(s):
            if char_index_dict[c][-1] > i:
                continue
            else:
                unique_s += c

        return unique_s


s = Solution()
print(s.removeDuplicateLetters("bcabc"))
