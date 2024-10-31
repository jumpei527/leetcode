# Time: O(m + n)
# Space: O(1)
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = m - 1
        k = n - 1
        for i in range(m + n - 1, -1, -1):
            if k == -1:
                break
            elif j >= 0 and nums1[j] > nums2[k]:
                nums1[i] = nums1[j]
                j -= 1
            else:
                nums1[i] = nums2[k]
                k -= 1
