# n = len(nums)
# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums_freq = {}

        for num in nums:
            nums_freq[num] = nums_freq.get(num, 0) + 1

        pairs_cnt = 0
        for num in nums_freq.keys():
            target_num = num + k
            if k == 0 and nums_freq[num] > 1:
                pairs_cnt += 1
            elif k != 0 and target_num in nums_freq:
                pairs_cnt += 1

        return pairs_cnt
