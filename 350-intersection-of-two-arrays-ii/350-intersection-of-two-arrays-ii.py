class Solution(object):
    def intersect(self, nums1, nums2):
        l=[]
        c1 = collections.Counter(nums1)
        res = []
        for num in nums2:
            if c1[num] > 0:
                c1[num] -= 1
                res.append(num)
                
        return res
        