class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #       recursion
        # def func(ind,prev_ind):
        #     if ind==len(nums):
        #         return 0
        #     no=func(ind+1,prev_ind)
        #     yes=0
        #     if prev_ind==-1 or nums[ind]>nums[prev_ind]:
        #         yes=1+func(ind+1,ind)
        #     return max(no,yes)
        # ans=func(0,-1)
        # return ans
        
        LIS=[1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    LIS[i]=max(LIS[i],1+LIS[j])
        return max(LIS)
        