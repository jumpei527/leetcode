# Time: O(n)
# Space: O(1)
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur_pos = 0

        for idx in range(1, len(nums)):
            if nums[idx] != nums[cur_pos]:
                cur_pos += 1
                nums[cur_pos] = nums[idx]

        return cur_pos + 1
