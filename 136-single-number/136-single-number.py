class Solution(object):
    def singleNumber(self, nums):
        for i in set(nums):
            nums.remove(i)
            if i not in nums:
                return i
        