class Solution(object):
    def twoSum(self, numbers, target):
        if len(numbers) == 2:
            return [1,2]
        
        s = 0
        e = len(numbers)-1
        res = 0
        while True:
            res = numbers[s]+numbers[e]
            if target == res:
                return [s+1,e+1]
            elif target < res:
                e-=1
            elif target > res:
                s+=1