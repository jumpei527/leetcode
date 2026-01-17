# n = len(prices)
# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []

        for idx, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                prices[stack.pop()] -= price
            stack.append(idx)

        return prices
