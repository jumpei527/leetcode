# n, m = len(word1), len(word2)
# Time: O(nm)
# Space: O(nm)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1_len, w2_len = len(word1), len(word2)
        edit_distance = [[0] * (w1_len+1) for _ in range(w2_len+1)]

        for i in range(w1_len+1):
            edit_distance[0][i] = i
        for j in range(w2_len+1):
            edit_distance[j][0] = j

        for i in range(1, w1_len+1):
            for j in range(1, w2_len+1):
                if word1[i-1] == word2[j-1]:
                    edit_cost = 0
                else:
                    edit_cost = 1
                edit_distance[j][i] = min(
                    edit_distance[j-1][i] + 1,
                    edit_distance[j][i-1] + 1,
                    edit_distance[j-1][i-1] + edit_cost
                )

        return edit_distance[-1][-1]
