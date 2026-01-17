# Time: O(logn)
# Space: O(1)


class Solution:
    def mySqrt(self, x: int) -> int:
        ok = -1
        ng = x + 1
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                ng = mid
            else:
                ok = mid
        return ok
