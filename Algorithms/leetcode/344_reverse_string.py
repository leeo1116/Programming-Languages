class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        i, j = 0, len(s)-1
        while i < j:
            s_list[i], s_list[j] = s_list[j], s_list[i]
            i += 1
            j -= 1

        return ''.join(s_list)

