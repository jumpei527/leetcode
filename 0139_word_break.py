# n = len(s)
# m = len(wordDict)
# Time: O(n * m)
# Space: O(n * m)
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)

        for i in range(len(s)+1):
            for w in wordDict:
                start = i - len(w)
                if start >= 0 and dp[start] and s[start:i] == w:
                    dp[i] = True

        return dp[-1]
