__doc__ = """
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and
there exists one unique longest palindromic substring.
"""

class Solution(object):
    def __init__(self, index):
        pass

    def longest_palindromic_substring(self, s):
        s_len = len(s)
        max_palindrome_len = 0
        palindrome = ''
        for i in range(s_len):
            if s_len-i-1 >= max_palindrome_len:
                for j in range(s_len-1, i-1, -1):
                    if j-i+1 > max_palindrome_len:
                        if self.is_palindrome(s[i:j+1]) and j-i+1 > max_palindrome_len:
                            max_palindrome_len = j-i+1
                            palindrome = s[i:j+1]
                            break
                    else:
                        break
        return palindrome

    def is_palindrome(self, s):
        i, j = 0, len(s)-1
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True


s = Solution(5)
print(s.longest_palindromic_substring('abc'))
