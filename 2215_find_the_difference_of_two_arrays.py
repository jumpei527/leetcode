# n = len(nums1)
# m = len(nums2)
# Time: O(n + m)
# Space: O(n + m)
from typing import List


class Solution:
    def findDifference(
        self, nums1: List[int], nums2: List[int]
    ) -> List[List[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        ans = [[], []]

        for num1 in nums1_set:
            if num1 not in nums2_set:
                ans[0].append(num1)

        for num2 in nums2_set:
            if num2 not in nums1_set:
                ans[1].append(num2)

        return ans
