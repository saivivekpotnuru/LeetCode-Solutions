from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        c=Counter(nums)
        d=[num for num,fre in c.items() if fre>len(nums)//2]
        return d[0]
            
        