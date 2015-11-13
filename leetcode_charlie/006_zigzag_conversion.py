__doc__ = """
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display
this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
Subscribe to see which companies asked this question
"""

class Solution(object):
    def __init__(self, index):
        pass

    def zigzag_conversion(self, s, n):
        if n <= 1:
            return s
        s_len = len(s)
        s_zigzag = ['']*n
        for i in range(s_len):
            row = i%(n+n-2)
            if n <= row < n+n-2:
                row = (n+n-2)-row
            s_zigzag[row] += s[i]
        s_zigzag = ''.join(s_zigzag)
        return s_zigzag

s = Solution(6)
print(s.zigzag_conversion("a", 1))

