class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        ans=0
        for end in range(start,len(s)):
            res=s[start:end+1]
            if len(res) == len(set(res)):
                ans=max(ans,len(res))
            else: start+=1
        return ans
            