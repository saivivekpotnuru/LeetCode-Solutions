class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        shortest = min(strs, key=len)

        for i in range(len(shortest)):
            for s in strs:
                if s[i] != shortest[i]:
                    return res
            res += strs[0][i]
        return res
        
        