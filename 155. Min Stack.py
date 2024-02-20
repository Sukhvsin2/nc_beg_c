class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minTrack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)

        if self.minTrack and val > self.minTrack[-1]:
            self.minTrack.append(self.minTrack[-1])
        else:
            self.minTrack.append(val)
            
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minTrack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minTrack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
