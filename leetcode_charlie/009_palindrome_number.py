__doc__ = """
Determine whether an integer is a palindrome. Do this without extra space.
"""

class Solution(object):
    def __init__(self, index):
        self.index = index

    def is_palindrome_number(self, x):
        if x != 0 and x % 10 == 0:
            return False
        x_reverse = 0
        while x > x_reverse:
            x_reverse = x_reverse*10+x % 10
            x //= 10
        return x == x_reverse or x == x_reverse//10

s = Solution(9)
print("Problem #{0}".format(s.index))
print(s.is_palindrome_number(1213))
