class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans=[]
        def bt(start,curr):
            if sum(curr)==target:
                ans.append(curr[:])
                return
            elif sum(curr)>target:
                return
            for i in range(start,len(candidates)):
                if i!=start and candidates[i]==candidates[i-1]:
                    continue
                curr.append(candidates[i])
                bt(i+1,curr)
                curr.pop()
        bt(0,[])
        return ans