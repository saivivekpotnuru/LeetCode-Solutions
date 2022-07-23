class Solution(object):
    def getRow(self, rowIndex):
        l=[0]*(rowIndex+1)
        l[0]=1
        for i in range(1,rowIndex+1):
            l[i]=int(l[i-1]*(rowIndex-i+1)/i)
        return l
            
          