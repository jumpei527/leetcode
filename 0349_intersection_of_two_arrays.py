from typing import List
# n = len(num1)
# m = len(num2)


class Solution:
    # Time: O(max(n*2, m*2))
    # Space: O(n + m)
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

class Solution2:
    # Time: O(n * m)
    # Space: O(min(n, m))
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        common_elements = set()
        for num in nums1:
            if num in nums2:
                common_elements.add(num)
        return list(common_elements)

class Solution3:
    # Time: O(n + m)
    # Space: O(n + m)
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)
