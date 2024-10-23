# Time: O(n + m)
# Space: O(n + m)
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict = {}
        intersection = []
        for n1 in nums1:
            if n1 not in dict.keys():
                dict[n1] = 1
        for n2 in nums2:
            if n2 in dict.keys() and n2 not in intersection:
                intersection.append(n2)
        return intersection
