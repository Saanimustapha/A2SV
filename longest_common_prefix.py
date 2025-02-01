class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        first = strs[0]
        last = strs[len(strs)-1]

        i,j = 0,0
        common = ""
        while i<len(first) and j<len(last):
            if first[i] == last[i]:
                common+=first[i]
                i+=1
                j+=1
            else:
                break
        return common
