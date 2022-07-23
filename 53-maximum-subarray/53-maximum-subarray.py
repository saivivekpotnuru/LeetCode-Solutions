class Solution(object):
    def maxSubArray(self, nums):
        maxSum = nums[0]
        prefixSum = 0
        
        for i in range(len(nums)):
            if prefixSum < 0:
                prefixSum = 0
            prefixSum += nums[i]
            maxSum = max(prefixSum, maxSum)
            
        return maxSum
        