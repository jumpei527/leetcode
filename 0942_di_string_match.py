# n = len(s)
# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        pending_nums = []
        ans = []

        for i in range(len(s)+1):
            pending_nums.append(i)

            if i == len(s) or s[i] == "I":
                while pending_nums:
                    digit = pending_nums.pop()
                    ans.append(digit)

        return ans
