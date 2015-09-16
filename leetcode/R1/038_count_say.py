__author__ = 'liangl2'
class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        current_num_str = '1'
        if n == 1:
            return current_num_str
        while n-1:
            new_num_str = self.count(current_num_str)
            current_num_str = new_num_str
            n -= 1
        return new_num_str

    def count(self, num_str):
        i, j, k = 0, 0, 0
        times = [0]*len(num_str)
        digits = ['']*len(num_str)
        while i < len(num_str):
            tmp = num_str[i]
            while i < len(num_str) and num_str[i] == tmp:
                times[j] += 1
                digits[j] = tmp
                i += 1
            j += 1
        num_str_count = ['']*len(digits)
        while k < len(times) and times[k] != 0:
            num_str_count[k] = str(times[k])+digits[k]
            k += 1
        return ''.join(num_str_count)

s = Solution()
print(s.countAndSay(7))