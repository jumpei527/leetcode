# n = len(items)
from collections import defaultdict
from typing import List
import heapq


class Solution:
    # Time: O(nlogn)
    # Space: O(n)
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        score_map = defaultdict(list)
        for id, score in items:
            score_map[id].append(score)

        ans = []
        for id, score_list in score_map.items():
            score_list.sort(reverse=True)
            total = 0
            for idx in range(5):
                total += score_list[idx]
            avg = total // 5
            ans.append([id, avg])

        return ans


class Solution2:
    # Time: O(n)
    # Space: O(n)
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        score_map = defaultdict(list)
        for id, score in items:
            heapq.heappush(score_map[id], score)
            if len(score_map[id]) > 5:
                heapq.heappop(score_map[id])

        ans = []
        for id in sorted(score_map):
            avg = sum(score_map[id]) // 5
            ans.append([id, avg])

        return ans
