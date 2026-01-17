# n is the last day in days
# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1]
        min_costs = [0] * (last_day + 1)
        travelling_day = set(days)

        for i in range(1, last_day + 1):
            if i not in travelling_day:
                min_costs[i] = min_costs[i-1]
            else:
                cost_1day = min_costs[max(0, i-1)] + costs[0]
                cost_7day = min_costs[max(0, i-7)] + costs[1]
                cost_30day = min_costs[max(0, i-30)] + costs[2]

                min_costs[i] = min(cost_1day, cost_7day, cost_30day)

        return min_costs[-1]
