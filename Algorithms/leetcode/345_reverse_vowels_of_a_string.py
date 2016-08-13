class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        flag_list = [0]*len(s)
        for i in range(len(s)):
            if s[i].upper() in 'AEIOU':
                flag_list[i] = 1

        i, j = 0, len(s)-1
        while i < j:
            if flag_list[i] == 1 and flag_list[j] == 1:
                s_list[i], s_list[j] = s_list[j], s_list[i]
                i += 1
                j -= 1
            elif flag_list[i] == 1 and flag_list[j] != 1:
                j -= 1
            elif flag_list[i] != 1 and flag_list[j] == 1:
                i += 1
            else:
                i += 1
                j -= 1

        return ''.join(s_list)


s = Solution()
print(s.reverseVowels('aA'))

