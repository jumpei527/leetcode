# n = len(arr)
# Time: O(nlogn)
# Space: O(n)
from typing import List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        nums_freq = {}
        for num in arr:
            nums_freq[num] = nums_freq.get(num, 0) + 1

        sorted_arr = sorted(arr, key=abs)
        for num in sorted_arr:
            if nums_freq[num] == 0:
                continue
            if nums_freq.get(2 * num, 0) == 0:
                return False

            nums_freq[num] -= 1
            nums_freq[2 * num] -= 1

        return True
