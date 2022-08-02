class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        ds={}
        dt={}
        for i in s:
            if i not in ds:
                ds[i]=1
            else:
                ds[i]+=1
        for i in t:
            if i not in dt:
                dt[i]=1
            else:
                dt[i]+=1
        for i in ds:
            if i not in dt:
                return False
            elif ds[i]!=dt[i]:
                return False
        return True
                