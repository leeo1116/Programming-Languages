__author__ = 'Liang Li'
class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        integer_str = ""
        sign = 0
        min_int, max_int = -1 << (32-1), (1 << (32-1))-1
        last_i = 0
        for i in range(len(str)):
            if integer_str == "" and (not (ord('0') <= ord(str[i]) <= ord('9') or str[i] in {'+', '-'})) and str[i] != ' ':
                return 0
            if integer_str == "" and (not ord('0') <= ord(str[i]) <= ord('9')) and sign != 0:
                return 0
            if (integer_str != "" or sign != 0) and (not ord('0') <= ord(str[i]) <= ord('9')):
                if sign == 0:
                    sign = 1
                integer = int(integer_str)*sign if integer_str != "" else 0
                return (integer > max_int)*max_int + (integer < min_int)*min_int + (min_int <= integer <= max_int)*integer if str != "" else 0
            if str[i] == '-':
                if sign == 1:
                    return 0
                sign = -1
            if str[i] == '+':
                if sign == -1:
                    return 0
                sign = 1

            if ord('0') <= ord(str[i]) <= ord('9'):
                if (i - last_i) > 1:
                    return 0
                integer_str += str[i]
            last_i = i
        if sign == 0:
            sign = 1

        integer = int(integer_str)*sign if integer_str != "" else 0
        return (integer > max_int)*max_int + (integer < min_int)*min_int + (min_int <= integer <= max_int)*integer if str != "" else 0




s = Solution()
i = s.myAtoi(" +1")
print(i)