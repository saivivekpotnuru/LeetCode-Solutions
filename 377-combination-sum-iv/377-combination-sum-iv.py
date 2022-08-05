class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=[-1 for i in range(target+1)]
        def dfs(target):
            if target<0:
                return 0
            if target==0:
                return 1 
            if dp[target] != -1:
                return dp[target]
            s=0
            for i in range(len(nums)):
                s += dfs(target-nums[i])
            dp[target]=s
            return dp[target]
        
        return dfs(target)
