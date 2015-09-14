__author__ = 'Liang Li'
class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        n1 = len(num1)
        n2 = len(num2)

        # sum_tmp = 0
        sum_total = 0
        factor = 1
        for i in range(n1-1, -1, -1):
            carry_in = 0
            sum_list = [0]*(n2+1)
            for j in range(n2-1, -1, -1):
                tmp = int(num1[i])*int(num2[j])+carry_in
                carry_in = tmp//10
                sum_list[j+1] = tmp % 10
            sum_list[0] = carry_in
            sum_tmp = int(''.join(map(str, sum_list)))
            sum_total += sum_tmp*factor
            factor *= 10
        return str(sum_total)


s = Solution()
print(s.multiply("62143823", "239"))

