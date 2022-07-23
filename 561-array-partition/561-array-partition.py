class Solution(object):
    def arrayPairSum(self, nums):
        s=0
        nums.sort()
        for i in range(0,len(nums),2):
            s+=(min(nums[i:i+2]))
        return s