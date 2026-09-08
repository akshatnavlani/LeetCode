class Solution:
    def romanToInt(self, s: str) -> int:
        ans,num,pre=0,0,0
        for i in reversed(s):
            if i=="M": num=1000
            if i=="D": num=500
            if i=="C": num=100
            if i=="L": num=50
            if i=="X": num=10
            if i=="V": num=5
            if i=="I": num=1

            if num<pre:
                ans-=num
            else:
                ans+=num
            pre=num
        return ans