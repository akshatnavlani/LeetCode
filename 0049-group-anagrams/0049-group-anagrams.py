class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs==[""]:
            return [[""]]
        sets={}
        for word in strs:
            letters=list(word)
            letters=str(sorted(letters))
            if letters not in sets:
                sets[letters]=[word]
            else:
                sets[letters]+=[word]
        return list(sets.values())
            