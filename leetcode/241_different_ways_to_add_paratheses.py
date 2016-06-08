class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        result = []
        for i in range(len(input)):
            if input[i] == '+' or input[i] == '-' or input[i] == '*':
                left_result = self.diffWaysToCompute(input[:i])
                right_result = self.diffWaysToCompute(input[i + 1:])
                for l in left_result:
                    for r in right_result:
                        result.append(self.diff_ways_to_compute_helper(l, r, input[i]))
        return result

    def diff_ways_to_compute_helper(self, operator1, operator2, operand):
        if operand == '+':
            return operator1 + operator2
        if operand == '-':
            return operator1 - operator2
        if operand == '*':
            return operator1 * operator2
            # or use eval("2*3")

s = Solution()
print(s.diffWaysToCompute("2-1-1"))