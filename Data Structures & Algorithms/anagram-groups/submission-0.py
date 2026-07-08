class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map=defaultdict(list)
        for i in strs:
            if i not in map.values():
                s=''.join(sorted(i))
                print(s)
                map[s].append(i)
        return list(map.values())