class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        c=0
        x=len(nums)
        if x==1:
            return nums
        for i in range(x):
            if(nums[i]==0 and i!=x-1):
                nums[i-c]=nums[i+1]
                c+=1
                continue
            nums[i-c]=nums[i]
        for i in range(x-c,x):
            nums[i]=0
        