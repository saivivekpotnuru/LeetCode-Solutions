class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        prev=[0 for i in range(n)]
        
        for i in range(m):
            cur=[0 for i in range(n)]
            for j in range(n):
                if i==0 and j==0:
                    cur[j]=1
                    continue
                up=left=0
                if i>0:
                    up=prev[j]
                if j>0:
                    left=cur[j-1]
                cur[j]=up+left
            prev=cur  
        return prev[n-1]
    
        