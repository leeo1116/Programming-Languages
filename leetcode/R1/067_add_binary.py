__author__ = 'liangl2'
class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        max_len = max(len(a), len(b))
        digit_sum = [0]*max_len
        carry_in = [0]*max_len
        i, j = len(a)-1, len(b)-1
        while i >= 0 or j >= 0:
            k = max(i, j)
            d1 = a[i] if i >= 0 else '0'
            d2 = b[j] if j >= 0 else '0'
            digit_sum[k] = (int(d1)+int(d2)+carry_in[k])%2
            if k > 0:
                carry_in[k-1] = (int(d1)+int(d2)+carry_in[k])//2
                i -= 1
                j -= 1
            else:
                if (int(d1)+int(d2)+carry_in[k])//2 == 1:
                    digit_sum = [1]+digit_sum
                return ''.join(str(x) for x in digit_sum)
s = Solution()
print(s.addBinary('11', '111'))


