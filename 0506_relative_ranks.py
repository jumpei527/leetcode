# n = len(score)
from typing import List
from heapq import heappush, heappop


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Time: O(n^2)
        # Space: O(n)
        sorted_score = sorted(score, reverse=True)
        ans = []
        for n in score:
            rank = str(sorted_score.index(n) + 1)
            if rank == "1":
                rank = "Gold Medal"
            elif rank == "2":
                rank = "Silver Medal"
            elif rank == "3":
                rank = "Bronze Medal"
            ans.append(rank)
        return ans

    def findRelativeRanks2(self, score: List[int]) -> List[str]:
        # Time: O(nlogn)
        # Space: O(n)
        rank_dic = {}
        ans = []
        sorted_score = sorted(score, reverse=True)

        for i in range(len(score)):
            if i == 0:
                rank_dic[sorted_score[i]] = "Gold Medal"
            elif i == 1:
                rank_dic[sorted_score[i]] = "Silver Medal"
            elif i == 2:
                rank_dic[sorted_score[i]] = "Bronze Medal"
            else:
                rank_dic[sorted_score[i]] = str(i+1)

        for n in score:
            ans.append(rank_dic[n])
        return ans

    def findRelativeRanks3(self, score: List[int]) -> List[str]:
        # Time: O(nlogn)
        # Space: O(n)
        ans = [0] * len(score)
        heap = []
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"]

        for score_i, num in enumerate(score):
            heappush(heap, (-num, score_i))

        number = 1
        while heap:
            s, score_i = heappop(heap)
            if number < 4:
                ans[score_i] = rank[number-1]
            else:
                ans[score_i] = str(number)
            number += 1
        return ans
