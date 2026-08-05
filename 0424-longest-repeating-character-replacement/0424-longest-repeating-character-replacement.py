class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        freq=defaultdict(int)
        res=0
        for r in range(len(s)):
            freq[s[r]]+=1
            maxfreq=max(freq.values())
            while (r-l+1)-maxfreq > k:
                freq[s[l]]-=1
                l+=1
                maxfreq=max(freq.values())
            res=max(res,r-l+1)
        return res