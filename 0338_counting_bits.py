# N = len(n)
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # Time: O(NlogN)
        # Space: O(N)
        ans = []
        for i in range(n+1):
            count = 0
            while i > 0:
                count += i % 2
                i = i // 2
            ans.append(count)
        return ans


    def countBits2(self, n: int) -> List[int]:
        # Time: O(N)
        # Space: O(N)
        ans = [0] * (n+1)
        for i in range(1, n+1):
            ans[i] = ans[i // 2] + i % 2
        return ans
