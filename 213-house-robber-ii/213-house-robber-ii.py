class Solution(object):
    def rob(self, nums):
        def helper(arr):
            prev=arr[0]
            prev2=0
            for i in range(1,len(arr)):
                take= arr[i]
                if i>1:
                    take+=prev2
                nottake=0+prev
                
                cur=max(take,nottake)
                prev2=prev
                prev=cur
            return prev
        if len(nums)==1:
            return nums[0]
        return max(nums[0],helper(nums[1:]),helper(nums[:-1]))
                
                
            
        