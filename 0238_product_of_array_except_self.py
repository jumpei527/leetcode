# n = len(nums)
# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_cnt = 0
        for n in nums:
            if n == 0:
                zero_cnt += 1
            else:
                total_product *= n

        if zero_cnt >= 2:
            for i in range(len(nums)):
                nums[i] = 0
            return nums

        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = total_product
            elif zero_cnt == 1:
                nums[i] = 0
            else:
                nums[i] = total_product // nums[i]

        return nums
