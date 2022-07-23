class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1=nums1+nums2
        nums1.sort()
        median=0
        l=len(nums1)
        if len(nums1)%2==0:
            median=(nums1[l//2]+nums1[(l//2)-1])/2
        else:
            median=nums1[l//2]
        return median