class Solution(object):
    def findDuplicate(self, nums):
        l=[0]*len(nums)
        for i in nums:
            l[i-1]+=1
        for i in range(len(l)):
            if l[i]>1:
                return i+1
            
        
        