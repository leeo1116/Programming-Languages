__doc__ = """
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""


class Solution(object):
    def __init__(self, index):
        self.index = index

    def reverse_integer(self, x):
        sign = 1 if x > 0 else -1
        x *= sign
        new_x, new_x_tmp = 0, 0
        while x:
            new_x = new_x*10+(x % 10)
            # Overflow check
            if (new_x-x % 10)//10 != new_x_tmp:
                return 0
            new_x_tmp = new_x
            x //= 10
        return new_x*sign

    def reverse_integer_python(self, x):
        sign = 1 if x > 0 else -1
        x *= sign

        max_int = (1 << 31)-1
        min_int = -(1 << 31)
        new_x = 0
        while x:
            new_x = new_x*10+x%10
            x //= 10
        if new_x*sign > max_int or new_x*sign < min_int:
            return 0
        else:
            return new_x*sign
        

s = Solution(7)
print(s.reverse_integer_python(1463847412))
