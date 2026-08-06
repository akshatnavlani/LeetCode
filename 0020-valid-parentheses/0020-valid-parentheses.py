class Solution:
    def isValid(self, s: str) -> bool:
        arr=[]
        for i in s:
            if i=='{' or i=='[' or i=='(':
                arr.append(i)
                continue
            if arr==[]:return False
            if (arr[-1]=='{' and i=='}') or (arr[-1]=='[' and i==']') or(arr[-1]=='('and i==')'):
                arr.pop()
                continue
            else: 
                arr.append(i)
        if arr==[]:return True
        return False 


