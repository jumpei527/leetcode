# n = len(nums)
# Time: O(nlogn)
# Space: O(n)
from typing import List
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []

        for n in nums:
            if not res or res[-1] < n:
                res.append(n)
            else:
                idx = bisect.bisect_left(res, n)
                res[idx] = n

        return len(res)
