import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean=re.sub(r'[^\w\s]','',s)
        q=clean.replace(" ","").lower()
        print(q)
        for i in range(len(q)//2):
            if q[i] != q[len(q)-1-i]:
                print(i)
                return False
        return True
            
