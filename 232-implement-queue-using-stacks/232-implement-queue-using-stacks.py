class MyQueue(object):

    def __init__(self):
        self.l=list()
        

    def push(self, x):
        self.l.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if self.l:
            return self.l.pop(0)
        else:
            return -1
    def peek(self):
        """
        :rtype: int
        """
        if self.l:
            return self.l[0]
        else:
            return -1
    def empty(self):
        """
        :rtype: bool
        """
        if self.l:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()