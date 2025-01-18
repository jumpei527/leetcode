# m, n = len(s1),  len(s2)
# Time: O(mn)
# Space: O(mn)


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1),  len(s2), len(s3)
        if m + n != l:
            return False
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True

        for i in range(1, m+1):
            if dp[i-1][0] and s1[i-1] == s3[i-1]:
                dp[i][0] = True

        for j in range(1, n+1):
            if dp[0][j-1] and s2[j-1] == s3[j-1]:
                dp[0][j] = True

        for i in range(1, m+1):
            for j in range(1, n+1):
                if dp[i-1][j] and s1[i-1] == s3[i+j-1]:
                    dp[i][j] = True
                if dp[i][j-1] and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = True

        return dp[-1][-1]
