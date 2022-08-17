class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        lcp=""      #result
        minlen=len(min(strs,key=len))
        i=0
        
        while i<minlen:
            char=strs[0][i]
            
            for j in range(1,len(strs)):
                if char != strs[j][i]:
                    return lcp
            lcp+=char
            i+=1
        return lcp
        
        
        