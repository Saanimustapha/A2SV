class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLenStr = min(len(string) for string in strs)
        commonIndex = 0

        if "" in strs:
            return ""
        
        for i in range(minLenStr):
            for j in range(1,len(strs)):
                if strs[j][i] != strs[0][i]:
                    return "" if i==0 else strs[0][0:commonIndex+1]
            commonIndex = i
        return strs[0][0:commonIndex+1]
