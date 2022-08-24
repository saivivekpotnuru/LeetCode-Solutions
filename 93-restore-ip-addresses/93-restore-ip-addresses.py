class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res=[]
        
        if len(s)>12:
            return res
        
        def backtracking(i,dots,curIp):
            if dots==4 and i==len(s):
                res.append(curIp[:-1])#-1 for removing last .
                return 
            
            if dots>4:
                return 
            
            for j in range(i, min(i+3,len(s))):
                #we need to go if substring is less than 255 and there should be no leading zeroes
                #for that i have checked whether i==j that is string len 1 or s[i]!="0" no starting zero
    
                if int(s[i:j+1])<256 and ((i==j) or s[i]!="0"):
                    backtracking(j+1,dots+1,curIp+s[i:j+1]+".")
                
                
        backtracking(0,0,"")
        return res
        