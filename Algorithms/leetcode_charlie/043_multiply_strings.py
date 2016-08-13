class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry_in, digit_sum, factor, sum_total = 0, 0, 1, 0

        for d2 in range(len(num2)-1, -1, -1):
            carry_in = 0
            sum_tmp_list = [0]*(len(num1)+1)
            for d1 in range(len(num1)-1, -1, -1):
                tmp = carry_in+int(num1[d1])*int(num2[d2])
                sum_tmp_list[d1+1] = tmp % 10
                carry_in = tmp//10
            sum_tmp_list[0] = carry_in
            sum_tmp = int(''.join(map(str, sum_tmp_list)))
            sum_total += sum_tmp*factor
            factor *= 10
        return str(sum_total)
