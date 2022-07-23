class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # n=len(nums)-1
        # dp=[False for i in range(len(nums))]
        # for i in range(n-1,-1,-1):
        #     if nums[i]+i>=n:
        #         dp[i]=True
        # return dp[0]
        
        goal=len(nums)-1
        
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i]>=goal:
                goal=i
        return True if goal==0 else False