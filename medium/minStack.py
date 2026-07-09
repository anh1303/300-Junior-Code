class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = 1e7

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        if len(self.stack) == 0:
            self.min = value
            self.stack.append(value)
            return
        
        if value < self.min:
            self.stack.append(2*value - self.min)
            self.min = value
        else:
            self.stack.append(value)

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) == 0:
            return
        
        if self.stack[-1] >= self.min:
            self.stack.pop()
        else:
            self.min = 2 * self.min - self.stack[-1]
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        
        if self.stack[-1] >= self.min:
            return self.stack[-1]
        else:
            return self.min

    def getMin(self):
        """
        :rtype: int
        """
        return self.min



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()