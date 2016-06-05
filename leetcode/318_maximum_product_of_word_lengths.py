class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        # words_len = len(words)
        # max_prod_len = 0
        # for i in range(words_len):
        #     char_flag_dict = {}
        #     for i_char in words[i]:
        #         char_flag_dict[i_char] = 1
        #     for j in range(i+1, words_len):
        #         flag = 0
        #         for j_char in words[j]:
        #             if char_flag_dict.get(j_char, None):
        #                 flag = 1
        #                 break
        #         if flag:
        #             continue
        #         else:
        #             max_prod_len = max(max_prod_len, len(words[i])*len(words[j]))
        # return max_prod_len

        # words_len = len(words)
        # char_stat_list = [0]*words_len
        # max_len_prod = 0
        # for i, word in enumerate(words):
        #     for char in word:
        #         char_stat_list[i] |= 1 << (ord(char) - ord('a'))
        #
        # for j in range(words_len):
        #     for k in range(j+1, words_len):
        #         if char_stat_list[j] & char_stat_list[k] == 0:
        #             max_len_prod = max(max_len_prod, len(words[j]*len(words[k])))
        #
        # return max_len_prod

        words_len = len(words)
        char_stat_list = [0] * words_len
        max_len_prod = 0
        words = sorted(words, key=len)
        for i, word in enumerate(words):
            for char in word:
                char_stat_list[i] |= 1 << (ord(char) - ord('a'))

        for j in range(words_len):
            for k in range(j + 1, words_len):
                if char_stat_list[j] & char_stat_list[k] == 0:
                    max_len_prod = max(max_len_prod, len(words[j] * len(words[k])))

        return max_len_prod

s = Solution()
print(s.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))