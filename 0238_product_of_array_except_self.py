# n = len(nums)
# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        prefix_product = 1
        for idx in range(len(nums)):
            ans[idx] = prefix_product
            prefix_product *= nums[idx]

        suffix_product = 1
        for idx in range(len(nums) - 1, -1, -1):
            ans[idx] *= suffix_product
            suffix_product *= nums[idx]

        return ans
