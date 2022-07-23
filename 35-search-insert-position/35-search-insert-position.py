class Solution(object):
    def searchInsert(self, nums, target):
        try:
            return nums.index(target)
        except:
            for i in range(0,len(nums)):
                if nums[i]>target:
                    return i
            return len(nums)
        
        
        
        
        
        