# Time: O(klogk)
# Space: O(k)
from typing import List
import heapq


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        pairs_arr = []
        if not nums1 or not nums2 or k == 0:
            return pairs_arr
        pair_sum_heap = []

        for idx in range(min(k, len(nums1))):
            heapq.heappush(pair_sum_heap, [nums1[idx] + nums2[0], idx, 0])

        while k > 0 and pair_sum_heap:
            _, num1_pos, num2_pos = heapq.heappop(pair_sum_heap)

            pairs_arr.append([nums1[num1_pos], nums2[num2_pos]])
            if num2_pos+1 < len(nums2):
                heapq.heappush(
                    pair_sum_heap,
                    [nums1[num1_pos] + nums2[num2_pos+1], num1_pos, num2_pos+1]
                )
            k -= 1

        return pairs_arr
