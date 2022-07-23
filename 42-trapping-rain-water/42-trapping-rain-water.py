class Solution(object):
    def trap(self, height):
        if not height:
            return 0
        l=0
        r=len(height)-1
        res=0
        leftMax,rightMax=height[l],height[r]
        while l<r:
            if leftMax<rightMax:
                l+=1
                leftMax=max(leftMax,height[l])
                res+= leftMax-height[l]
            else:
                r-=1
                rightMax=max(rightMax,height[r])
                res+= rightMax-height[r]
        return res
                
       
        
        