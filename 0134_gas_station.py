# n = len(gas)
# Time: O(n)
# space: O(1)
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        current_gas = 0
        start_idx = 0

        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]
            if current_gas < 0:
                current_gas = 0
                start_idx = i + 1

        return start_idx
