class Solution(object):
    def subsets(self, nums):
        final=[]
        def func(nums,index,current):
            if index==len(nums):
                final.append(current)
                return 
            func(nums,index+1,current)
            func(nums,index+1,current+[nums[index]])
            
        
        
        func(nums,0,[])
        return final
        