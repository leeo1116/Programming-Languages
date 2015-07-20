__author__ = 'Liang Li'
class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        roman_numeral = ['', 'I', "II", "III", "IV", "V", "VI", "VII", "VIII", "IX",
                         '', 'X', "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC",
                         '', 'C', "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM",
                         '', 'M', "MM", "MMM"]
        return str(roman_numeral[num//1000+30]+roman_numeral[(num%1000)//100+20]
                   +roman_numeral[(num%100)//10+10]+roman_numeral[num%10])


s = Solution()
print(s.intToRoman(2929))