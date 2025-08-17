# n = len(nums)
# Time: O(nlogn)
# Space: O(n)
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_length = len(nums)
        sorted_nums = sorted(nums)

        large_group_ptr = nums_length - 1
        small_group_ptr = (nums_length - 1) // 2

        for idx in range(len(nums)):
            if idx % 2 == 0:
                nums[idx] = sorted_nums[small_group_ptr]
                small_group_ptr -= 1
            else:
                nums[idx] = sorted_nums[large_group_ptr]
                large_group_ptr -= 1

        return
