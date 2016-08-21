class Solution:
    # @param str: a string
    # @return an integer
    def atoi(self, str):
        """
        Convert a string to integer
        :param str: input string, which may not be valid
        :return: corresponding integer
        """
        if len(str) == 0:
            return 0
        sign, num, p = 1, 0, 0
        min_int, max_int = -1 << 31, (1 << 31)-1
        while str[p] == ' ':
            p += 1
        if str[p] == '-' or str[p] == '+':
            sign = 1 if str[p] == '+' else 0
            p += 1
        while p < len(str) and '0' <= str[p] <= '9':
            num = num*10+ord(str[p])-ord('0')
            num_tmp = num if sign else -num
            if num_tmp < min_int:
                return min_int
            if num_tmp > max_int:
                return max_int
            p += 1
        return num if sign else -num




