class Solution(object):
    def update_bits_m0(self, n, m, i, j):
        ones = ~0
        if j < 31:
            left = ones << (j+1)
            right = (1 << i)-1
            mask = left | right
        else:
            mask = (1 << i)-1
        return (n & mask) | (m << i)

    def update_bits_m1(self, n, m, i, j):
        mask = ~(1<<(j+1)-(1<<i)) if j < 31 else (1 << i)-1
        return (m << i) | (mask & n)
