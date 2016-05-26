class Solution(object):
    def palindromePairs_brute_force(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        p_list = []
        words_len = len(words)
        for i in range(words_len):
            for j in range(i+1, words_len):
                if self.is_palindrome(words[i]+words[j]):
                    p_list.append([i, j])
                if self.is_palindrome(words[j]+words[i]):
                    p_list.append([j, i])
        return p_list

    def palindrome_pairs(self, words):
        word_index_dict = {}
        for i, w in enumerate(words):
            word_index_dict[w] = i

        p_list = []
        for j, word in enumerate(words):
            for k in range(len(word)+1):
                s1 = word[:k]
                s2 = word[k:]
                if self.is_palindrome(s2) and word_index_dict.get(s1[::-1], j) != j:
                    p_list.append([word_index_dict.get(s1[::-1]), j])
                if self.is_palindrome(s1) and word_index_dict.get(s2[::-1], j) != j and len(s2):
                    p_list.append([j, word_index_dict.get(s2[::-1])])
        return p_list

    @staticmethod
    def is_palindrome(word):
        i, j = 0, len(word)-1
        while i < j and word[i] == word[j]:
            i += 1
            j -= 1
        return i >= j


s = Solution()
print(s.palindromePairs_brute_force(["abcd","dcba","lls","s","sssll", "abb", "a", "c", "bd"]))
print(s.palindrome_pairs(["a",""]))




