class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_count_dict = {}
        for char1 in s:
            char_count_dict[char1] = char_count_dict.get(char1, 0) + 1
        for char2 in t:
            char_count_dict[char2] = char_count_dict.get(char2, 0) - 1
        for count in char_count_dict.values():
            if count != 0:
                return False
        return True
