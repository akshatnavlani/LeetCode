class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n+1)

        for stones in range(1, n+1):
            for i in range(1, int(stones**0.5)+1):
                if not dp[stones-i*i]:
                    dp[stones] = True
                    break

        return dp[n]