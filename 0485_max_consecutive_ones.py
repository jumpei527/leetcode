# n = len(nums)
# Time: O(n)
# Space: O(1)
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive_len = 0
        cur_len = 0
        for num in nums:
            if num == 1:
                cur_len += 1
                max_consecutive_len = max(cur_len, max_consecutive_len)
            else:
                cur_len = 0

        return max_consecutive_len
