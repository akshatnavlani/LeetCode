class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i=0
        tup=tuple(sorted(s1))
        j=len(s1)-1
        while j<=len(s2)-1:
            if (j-i+1) == len(s1):
                temp=tuple("".join(sorted(s2[i:j+1])))
                if temp == tup:
                    return True
            else:
                i+=1
                continue;
            j+=1
        return False
            


