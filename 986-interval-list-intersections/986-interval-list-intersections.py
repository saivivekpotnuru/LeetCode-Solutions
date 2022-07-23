class Solution(object):
    def intervalIntersection(self, firstlist, secondlist):
        a=0
        b=0
        intervals=[]
        while a<len(firstlist) and b<len(secondlist):
            interval_starting,interval_ending=max(firstlist[a][0],secondlist[b][0]),min(firstlist[a][1],secondlist[b][1])
            if interval_starting<=interval_ending:
                intervals.append([interval_starting,interval_ending])
            if firstlist[a][1]<secondlist[b][1]:
                a+=1
            else:
                b+=1
        return intervals