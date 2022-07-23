class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        final=[]
        nums.sort()
        def func(index,current):
            final.append(current[:])
            for i in range(index,len(nums)):
                if i>index and nums[i]==nums[i-1]:
                    continue
                current.append(nums[i])
                func(i+1,current)
                current.pop()
            
            
        
        
        func(0,[])
        return final

        