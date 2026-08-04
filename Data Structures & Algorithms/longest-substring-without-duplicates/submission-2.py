class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        ans=[]
        for end in range(start,len(s)):
            res=s[start:end+1]
            if len(res) == len(set(res)) and len(res)>len(ans):
                ans=res
            else: start+=1
        return len(ans)
            