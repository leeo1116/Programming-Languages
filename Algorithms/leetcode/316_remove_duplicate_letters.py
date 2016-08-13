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

        index_to_remove = []
        unique_s = ""

        for i, c in enumerate(s):
            if char_index_dict[c] > 1:
                j = i
                while char_index_dict.get(s[j], 0) > 1:
                    j += 1
                if c > s[j]

        return unique_s