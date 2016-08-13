class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def find_substring(self, s, words):
        if not words or not s:
            return []

        s_len = len(s)
        word_num = len(words)
        word_len = len(words[0])

        if s_len < word_num*word_len:
            return []

        # use dictionary to store the word count
        words_dict = {}
        for w in words:
            if words_dict.get(w, None):
                words_dict[w] += 1
            else:
                words_dict[w] = 1

        i = 0
        indices = []
        # traverse s with len(words)*len(each word) characters
        while i <= (s_len-word_len*word_num+1):
            s_dict = {}
            j = i
            while j < i+word_len*word_num:
                if s[j:j+word_len] in words_dict.keys():
                    if s_dict.get(s[j:j+word_len], None):
                        s_dict[s[j:j+word_len]] += 1
                    else:
                        s_dict[s[j:j+word_len]] = 1
                    j += word_len
                else:
                    break
            if s_dict == words_dict:
                indices.append(i)
            i += 1
        return indices

s = Solution()
print(s.find_substring("abab", ["ab", "ba"]))
