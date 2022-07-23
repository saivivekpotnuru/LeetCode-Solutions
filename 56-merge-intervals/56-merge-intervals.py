class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        merge=[intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=merge[-1][1]:
                merge[-1][1]=max(intervals[i][1],merge[-1][1])
            else:
                merge.append(intervals[i])
        return merge
        
        