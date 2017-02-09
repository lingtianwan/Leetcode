# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.
#
# You may assume that the given expression is always valid.
#
# Some examples:
# "3+2*2" = 7
# " 3/2 " = 1
# " 3+5 / 2 " = 5
# Note: Do not use the eval built-in library function.


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = []
        oper = []
        num = ''
        for i in s:
            if i.isdigit():
                num += i
            elif i in ('+', '-', '*', '/'):
                nums.append(int(num))
                num = ''
                oper.append(i)
        nums.append(int(num))
        i = 0
        while i < len(oper):
            if oper[i] == '*':
                nums[i] = nums[i] * nums[i+1]
                del nums[i+1]
                del oper[i]
            elif oper[i] == '/':
                nums[i] = nums[i] / nums[i+1]
                del nums[i+1]
                del oper[i]
            else:
                i += 1
        res = nums[0]
        for i in range(len(oper)):
            if oper[i] == '+':
                res += nums[i+1]
            else:
                res -= nums[i+1]
        return res
