class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # n=len(piles)
        # @cache
        # def maxDiff(i:int,j: int)->int:
        #     if i==j: return piles[i]
        #     return max(piles[i]-maxDiff(i+1,j),
        #                 piles[j]-maxDiff(i,j-1))

        # return maxDiff(0,n-1)>=0
        return True