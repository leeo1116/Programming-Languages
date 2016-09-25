class Solution(object):
    def binary_representation(self, n):
        sign = -1 if n[0] == '-' else 1
        integer_tmp, fraction_tmp = n.split('.')
        integer, fraction = int(integer_tmp), 10**(-len(fraction_tmp))*int(fraction_tmp)
        integer_str = self.decimal_to_binary_int(integer)
        fraction_str = self.decimal_to_binary_fraction(fraction)
        if fraction_str == "ERROR":
            return "ERROR"
        if fraction_str and integer_str:
            return integer_str+'.'+fraction_str if sign else '-'+integer_str+'.'+fraction_str
        elif integer_str:
            return integer_str if sign else '-'+integer_str
        elif fraction_str:
            return "0."+fraction_str if sign else "-0."+fraction_str
        else:
            return '0'

    @staticmethod
    def decimal_to_binary_int(integer):
        bits = []
        while integer:
            bits.insert(0, str(integer % 2))
            integer >>= 1
        return ''.join(bits)

    @staticmethod
    def decimal_to_binary_fraction(fraction):
        bits, fraction_backup = "", fraction
        while fraction != 0:
            fraction *= 2
            bits += str(int(fraction))
            fraction -= int(fraction)
            if len(bits) > 32:
                return "ERROR"
        return bits

s = Solution()
# print(s.binary_representation("17817287.6418609619140625"))
print(s.binary_representation("1"))