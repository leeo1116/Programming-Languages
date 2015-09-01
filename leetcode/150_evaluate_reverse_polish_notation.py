__author__ = 'liangl2'
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        token_stack = []
        operator_list = "+-*/"
        for token in tokens:
            if token not in operator_list:
                token_stack.append(token)
            else:
                operator = token
                operand1 = token_stack.pop()
                operand2 = token_stack.pop()
                result = self.operation(operator, int(operand1), int(operand2))
                token_stack.append(result)
        return int(token_stack[-1])

    def operation(self, operator, operand1, operand2):
        if operator == '+':
            return operand2+operand1
        elif operator == '-':
            return operand2-operand1
        elif operator == '*':
            return operand2*operand1
        elif operator == '/':
            return int(operand2/operand1)

s = Solution()
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))