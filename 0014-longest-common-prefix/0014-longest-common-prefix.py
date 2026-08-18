class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest=0
        if "" in strs:
            return ""
        m=min(strs)
        for i in range(len(m)):
            for j in strs:
                if j[i] != m[i]:
                    return m[0:i]
        return m