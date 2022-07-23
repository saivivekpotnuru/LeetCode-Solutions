class Solution(object):
    def generate(self, numRows):
        l=[[0 for j in range(i)] for i in range(1,numRows+1)]
        for i in range(numRows):
            l[i][0]=l[i][i]=1
            for j in range(1,i):
                l[i][j]=l[i-1][j]+l[i-1][j-1]
        return l
                    
        