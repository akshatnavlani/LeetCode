class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest=0
        profit=0
        for sell in range(len(prices)):
            profit= max(profit,prices[sell]-prices[lowest])
            if prices[sell]<prices[lowest]:
                lowest=sell
        return profit