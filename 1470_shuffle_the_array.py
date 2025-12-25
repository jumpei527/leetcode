# n = len(nums)
# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled_arr = []
        for idx in range(n):
            shuffled_arr.append(nums[idx])
            shuffled_arr.append(nums[idx + n])

        return shuffled_arr
