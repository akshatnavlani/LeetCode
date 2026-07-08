class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t): return False
        map_s=defaultdict()
        for i in range (len(s)):
            map_s[s[i]]=1+map_s.get(s[i],0)
            map_s[t[i]]=map_s.get(t[i],0)-1
        return all(v == 0 for v in map_s.values())
