class Solution:
    @staticmethod
    def count_bit_one(a):
        count = 0
        for i in range(32):
            if (a >> i) & 1 == 1:
                count += 1
        return count

    def bit_swap_required(self, a, b):
        return self.count_bit_one(a ^ b)

s = Solution()
print(s.bit_swap_required(1, 2))
