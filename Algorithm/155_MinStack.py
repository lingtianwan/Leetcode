# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.val = []
        self.min_val = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.val.append(x)
        if len(self.min_val) == 0 or self.min_val[-1] >= x:
            self.min_val.append(x)

    def pop(self):
        """
        :rtype: void
        """
        top = self.val[-1]
        self.val.pop()
        if self.min_val[-1] == top:
            self.min_val.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.val[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_val[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
