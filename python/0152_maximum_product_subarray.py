# n = len(nums)
# Time: O(n)
# Space: O(1)
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = max(nums)
        cur_max = 1
        cur_min = 1

        for num in nums:
            tmp = cur_max * num
            cur_max = max(tmp, cur_min * num, num)
            cur_min = min(tmp, cur_min * num, num)
            max_product = max(max_product, cur_max)

        return max_product
