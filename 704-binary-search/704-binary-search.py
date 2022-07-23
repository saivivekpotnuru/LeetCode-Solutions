class Solution(object):
    def search(self, nums, target):
        c=-1
        for i in nums:
            if target==i:
                c=nums.index(i)
                break
        else:
            c=-1
        return c
            
        