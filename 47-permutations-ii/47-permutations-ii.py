class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(i,current):
            if i==len(nums) and current not in res:
                res.append(current)
                return
            
            for j in range(i,len(nums)):
                copy=current.copy()
                temp=copy[j]
                copy[j]=copy[i]
                copy[i]=temp
                dfs(i+1,copy)
        dfs(0,nums)
        return res
        
        
        