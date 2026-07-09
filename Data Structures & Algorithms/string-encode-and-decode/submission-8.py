class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=""
        for i in strs:
            ans+=str(len(i))+'#'+i
        return ans
    def decode(self, s: str) -> List[str]:
        ans=[]
        l=0
        while(l<len(s)):
            r=l
            while(s[r]!='#'):
                r+=1
            leng= int(s[l:r])
            ans.append(s[r+1:r+leng+1])
            l=r+leng+1
        return ans
