class Solution(object):
    def maxProfit(self, prices):
        maxdiff=0
        minnum=float('inf')
        if prices==sorted(prices,reverse=True):
            return 0
        else:
            for i in range(len(prices)):
                minnum=min(minnum,prices[i])
                maxdiff=max(maxdiff,prices[i]-minnum)
            return maxdiff
                
                    
        