# n = len(text1)
# m = len(text2)
# Time: O(nm)
# Space: O(nm)


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1_length = len(text1)
        text2_length = len(text2)
        lcs_table = [[0] * (text2_length + 1) for _ in range(text1_length + 1)]

        for i in range(1, text1_length+1):
            for j in range(1, text2_length+1):
                if text1[i-1] == text2[j-1]:
                    lcs_table[i][j] = lcs_table[i-1][j-1] + 1
                else:
                    lcs_table[i][j] = max(lcs_table[i-1][j], lcs_table[i][j-1])

        return lcs_table[-1][-1]
