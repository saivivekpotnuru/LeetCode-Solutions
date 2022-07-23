class Solution(object):
    def plusOne(self, digits):
        nums1 = ""
        for i in digits:
            nums1 +=str(i)
        nums1 = int(nums1)
        nums1 +=1
        return [int(d) for d in str(nums1)]