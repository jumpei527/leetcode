# n = len(nums)
# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num_set = set(nums)
        disappeared_nums = []
        for num in range(1, len(nums) + 1):
            if num not in num_set:
                disappeared_nums.append(num)

        return disappeared_nums
