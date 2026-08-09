class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = [[0] * len(piles) for _ in range(len(piles))]
        suffixsum=[0]*len(piles)
        temp=0
        for i in range(len(piles)-1,-1,-1):
            temp+=piles[i]
            suffixsum[i]=temp
        return self.maxStone(suffixsum,1,0,memo)
    def maxStone(self,suffixSum :List[int], maxTillNow:int,currIndex:int,memo : List[List[int]]) -> int:
        if currIndex + 2 * maxTillNow >= len(suffixSum):
            return suffixSum[currIndex]
        if memo[currIndex][maxTillNow]>0:
            return memo[currIndex][maxTillNow]
        res = float("inf")
        for i in range(1,2*maxTillNow+1):
            res=min(res,self.maxStone(suffixSum,max(i,maxTillNow),currIndex+i,memo))
        memo[currIndex][maxTillNow]=suffixSum[currIndex]-res
        return memo[currIndex][maxTillNow]

        