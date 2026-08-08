import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        arr=[]
        while l<=r:
            speed=(l+r)//2
            total=0
            for i in piles:
                total+=math.ceil(i/speed)
            if total<=h:
                arr.append(speed)
                r=speed-1
            else:
                l=speed+1
        return min(arr)
