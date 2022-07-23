class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        for i in range(len(nums1)):
            f=0
            ind=nums2.index(nums1[i])
            for j in range(ind,len(nums2)):
                if nums2[j]>nums2[ind]:
                    nums1[i]=(nums2[j])
                    f=1
                    break
            if f==0:
                nums1[i]=-1
        return nums1