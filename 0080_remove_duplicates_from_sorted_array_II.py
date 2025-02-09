# n = len(n)
# Time: O(n)
# Space: O(1)
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        insert_position = 2

        for i in range(2, len(nums)):
            if nums[i] != nums[insert_position - 2]:
                nums[insert_position] = nums[i]
                insert_position += 1

        return insert_position
