# n = len(costs)
# Time: O(nlogn)
# Space: O(n)
from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0]-x[1])
        costs_length = len(costs)
        total_cost = 0

        for idx in range(costs_length // 2):
            total_cost += costs[idx][0]
        for idx in range(costs_length // 2, costs_length):
            total_cost += costs[idx][1]

        return total_cost
