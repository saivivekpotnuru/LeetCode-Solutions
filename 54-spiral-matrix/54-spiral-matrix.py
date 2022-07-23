class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row,col=len(matrix),len(matrix[0])
        t,b,l,r=0,row,0,col
        dir=0
        res=[]
        while l<r and t<b:
            if dir==0:
                for i in range(l,r):
                    res.append(matrix[t][i])
                t+=1
            elif dir==1:
                for i in range(t,b):
                    res.append(matrix[i][r-1])              
                r-=1
            elif dir==2:
                for i in range(r-1,l-1,-1):
                    res.append(matrix[b-1][i])
                b-=1
            else:
                for i in range(b-1,t-1,-1):
                    res.append(matrix[i][l])
                l+=1
            dir=(dir+1)%4
        return res
        