# Time: O(n)
# Space: O(1)


class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 0
        cur = 1
        for _ in range(n):
            cur, prev = prev + cur, cur
        return cur
