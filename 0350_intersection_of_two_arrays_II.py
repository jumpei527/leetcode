# n = len(nums1)
# m = len(nums2)
from typing import List
from collections import Counter


class Solution:
    # Time: O(nlogn + mlogm)
    # Space: O(min(n, m))
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                intersection.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return intersection


class Solution2:
    # Time: O(n + m)
    # Space: O(n + m)
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list((Counter(nums1) & Counter(nums2)).elements())
