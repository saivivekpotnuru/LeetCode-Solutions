class MyStack(object):

    def __init__(self):
        self.l=list()

    def push(self, x):
        self.l.append(x)
        """
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        if len(self.l)>0:
            return self.l.pop()
        """
        :rtype: int
        """
        

    def top(self):
        """
        :rtype: int
        """
        return self.l[-1]
        

    def empty(self):
        
        """
        :rtype: bool
        """
        if len(self.l)>0:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()