from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - buy_price)
            if buy_price > prices[i]:
                buy_price = prices[i]
        return profit
