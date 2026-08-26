class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count("1")<k:
            return ""
        ans=s
        l=c=0
        for r,ch in enumerate(s):
            c+=int(ch)
            while c>k or s[l]=="0":
                c-=int(s[l])
                l+=1
            if c==k:
                t=s[l:r+1]
                if len(t)<len(ans) or len(t)==len(ans) and t<ans:
                    ans=t
        return ans