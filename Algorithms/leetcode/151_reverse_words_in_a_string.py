class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        s_list = []
        word = ''
        for i, char in enumerate(s):
            if char == ' ':
                if not word:
                    continue
                else:
                    s_list.append(word)
                    word = ''
                    continue
            word += char
            if i == len(s) - 1:
                s_list.append(word)

        i, j = 0, len(s_list)-1
        while i < j:
            s_list[i], s_list[j] = s_list[j], s_list[i]
            i += 1
            j -= 1
        return ' '.join(s_list)

s = Solution()
print(s.reverseWords(" a b "))