class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        char_freq_dict = {}
        word_freq_dict = {}
        str_list = str.split()
        for word in str_list:
            word_freq_dict[word] = word_freq_dict.get(word, 0)+1
        for char in pattern:
            char_freq_dict[char] = char_freq_dict.get(char, 0)+1
        if len(char_freq_dict) != len(word_freq_dict):
            return False
        for i in range(len(char_freq_dict)):
            if char_freq_dict[pattern[i]] != word_freq_dict[str_list[i]]:
                return False
        return True

s = Solution()
print(s.wordPattern("abba", "dog cat cat dog"))