__author__ = 'liangl2'
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = self.remove_space(s)
        n = len(s)
        if n == 0:
            return False
        i = 0
        dot_flag, e_flag, has_digit, has_sign = False, False, False, False
        while i < n:
            if s[i].isdigit():
                i += 1
                has_digit = True
                has_sign = True
            elif not dot_flag and s[i] == '.':
                i += 1
                dot_flag = True
                has_sign = True
            elif has_digit and not e_flag and s[i].upper() == 'E':
                i += 1
                dot_flag = True
                e_flag = True
                has_digit = False
                has_sign = False
            elif not has_digit and not has_sign and (s[i] == '+' or s[i] == '-'):
                i += 1
                has_sign = True
            else:
                return False
        if has_digit:
            return True
        else:
            return False


    def remove_space(self, s):
        n = len(s)
        i, j = 0, n-1
        while i < n and s[i] == ' ':
            i += 1
        while j > -1 and s[j] == ' ':
            j -= 1
        return s[i:j+1]
