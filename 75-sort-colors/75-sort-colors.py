class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]>nums[j]:
        #             nums[i],nums[j]=nums[j],nums[i]
        num0 = 0
        num1 = 0
        num2 = 0
        for i in range(len(nums)):
            if nums[i]==0:
                num0 += 1
            if nums[i]==1:
                num1 += 1
            if nums[i]==2:
                num2 += 1

        for i in range(num0):
            nums[i]=0
        for i in range(num0,num0+num1):
            nums[i]=1
        for i in range(num0+num1,num0+num1+num2):
            nums[i]=2

        return nums
            
            