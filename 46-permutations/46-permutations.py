class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        freq=[False for i in range(len(nums))]
        ans=[]
        def dfs(current):
            if len(current)==len(nums):
                ans.append(current.copy())
                return 
            for i in range(len(nums)):
                if not freq[i]:
                    current.append(nums[i])
                    freq[i]=True
                    dfs(current)
                    freq[i]=False
                    current.pop()
        dfs([])    
        return ans