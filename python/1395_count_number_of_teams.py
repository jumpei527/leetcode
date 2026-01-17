# n = len(rating)
# Time: O(n^2)
# Space: O(1)
from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        num_soldiers = len(rating)
        if num_soldiers < 3:
            return 0

        total_teams = 0
        for j in range(1, num_soldiers - 1):
            left_smaller = 0
            left_larger = 0

            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                elif rating[i] > rating[j]:
                    left_larger += 1

            right_smaller = 0
            right_larger = 0

            for k in range(j+1, num_soldiers):
                if rating[j] > rating[k]:
                    right_smaller += 1
                elif rating[j] < rating[k]:
                    right_larger += 1

            total_teams += left_smaller * right_larger
            total_teams += left_larger * right_smaller

        return total_teams
