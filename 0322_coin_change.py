# n = len(coins)
# Time: O(n * amount)
# Space: O(amount)
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                start = i - coin
                if start >= 0 and dp[start] >= 0:
                    if dp[i] == -1:
                        dp[i] = dp[start] + 1
                    else:
                        dp[i] = min(dp[i], dp[start] + 1)
        return dp[amount]
