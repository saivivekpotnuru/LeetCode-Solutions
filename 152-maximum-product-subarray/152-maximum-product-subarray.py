class Solution:
    def maxProduct(self, nums: List[int]) -> int:
#         res=max(nums)
#         curmax,curmin=1,1
        
#         for i in nums:
#             temp=curmax*i
#             curmax=max(i*curmax,i*curmin,i)
#             curmin=(temp,i*curmin,i)
            
#             res=max(res,curmax)
#         return res
        res = max(nums)
        curMin, curMax = 1, 1
        
        for n in nums:
            
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n) 
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res