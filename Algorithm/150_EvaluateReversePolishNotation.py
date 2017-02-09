# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
# Some examples:
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        import operator
        operators = ['+', '-', '*', '/']
        op_map = {'+': operator.add, '-': operator.sub, '*': operator.mul}
        stack = []
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if i == '/':
                    stack.append(int(float(num2) / num1))
                else:
                    stack.append(op_map[i](num2, num1))
        return stack.pop()
