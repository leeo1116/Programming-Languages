__author__ = 'Liang Li'
class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        integer_str = ""
        neg_flag = 0
        pos_flag = 0
        integer = 0
        for c in str:
            if (integer_str != "" or neg_flag+pos_flag > 0) and (not c.isdigit()):
                if integer_str == "":
                    return 0
                else:
                    integer = int(integer_str)*(1-2*neg_flag)
                    return integer if 2**(32-1)-1 >= integer >= -2**(32-1) else 0
            if c == '-':
                neg_flag = 1
            if c == '+':
                pos_flag = 1
            if c.isdigit():
                integer_str += c
        if pos_flag and neg_flag:
            return 0
        if integer_str != "":
            integer = int(integer_str)*(1-2*neg_flag)
            if 2**(32-1)-1 >= integer >= -2**(32-1):
                return integer
            elif integer > 2**(32-1)-1:
                return 2**(32-1)-1
            else:
                return -2**(32-1)
        else:
            return 0


s = Solution()
i = s.myAtoi("   - 321")
print(i)