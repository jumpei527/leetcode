# n = len(nums)
# Time: O(n * n!)
# Space: O(n * n!)
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.permutation = []
        self.make_permutation(nums, [])
        return self.permutation

    def make_permutation(self, nums: List[int], sub: List[int]) -> None:
        if not nums:
            self.permutation.append(sub)
            return None

        for i, num in enumerate(nums):
            self.make_permutation(nums[:i] + nums[i+1:], sub + [num])
