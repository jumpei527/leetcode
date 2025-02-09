from typing import List
# n = len(nums)


class Solution:
    # Time: O(n)
    # Space: O(n)
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]


class Solution2:
    # Time: O(n)
    # Space: O(n)
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        nums_rotated = [0] * length

        for i in range(length):
            nums_rotated[(i + k) % length] = nums[i]

        nums[:] = nums_rotated
