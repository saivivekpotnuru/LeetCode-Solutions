class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i,j=0,len(nums)-1
        while i<=j:
            if nums[i]%2!=0 and nums[j]%2==0:
                t=nums[i]
                nums[i]=nums[j]
                nums[j]=t
                i+=1
                j-=1
            if nums[i]%2==0 and nums[j]%2!=0:
                i+=1
                j-=1
                
            if nums[i]%2==0:
                i+=1
            if nums[j]%2!=0:
                j-=1
            
        return nums
        