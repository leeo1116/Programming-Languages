__doc__ = """
Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution(object):
    def __init__(self, index):
        self.index = index

    def integer_to_roman(self, num):
        roman_symbol = ['', 'I', "II", "III", "IV", "V", "VI", "VII", "VIII", "IX",
                        '', 'X', "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC",
                        '', 'C', "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM",
                        '', 'M', "MM", "MMM"]
        return roman_symbol[num//1000+30]+roman_symbol[(num % 1000)//100+20] \
               + roman_symbol[(num % 100)//10+10]+roman_symbol[num % 10]
