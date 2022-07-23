class Solution(object):
    def rotate(self, nums, k):
        k=k%len(nums)
        if len(nums)==1 or k==0:
            pass
        else:
            l=nums[-k:]
            p=nums[:len(nums)-k]
            nums[:]=l+p
        
        