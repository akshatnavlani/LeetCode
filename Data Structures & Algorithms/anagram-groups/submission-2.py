class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map=defaultdict(list)
        for i in strs:
                s=''.join(sorted(i))
                map[s].append(i)
        return list(map.values())