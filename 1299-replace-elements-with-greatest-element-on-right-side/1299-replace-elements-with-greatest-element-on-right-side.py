class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr)==1:
            return [-1]
        m=arr[-1]
        arr[-1]=-1
        for i in range(len(arr)-2,-1,-1):
            if arr[i]>m:
                t=arr[i]
                arr[i]=m
                m=t
            else:
                arr[i]=m
        return arr

                
           
            
        