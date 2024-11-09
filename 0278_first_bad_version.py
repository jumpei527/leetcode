# Time: O(logn)
# Space: O(1)


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
def isBadVersion(version: int) -> bool:
    bad_version = 4
    return version >= bad_version


class Solution:
    def firstBadVersion(self, n: int) -> int:
        ok = -1
        ng = n

        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if isBadVersion(mid):
                ng = mid
            else:
                ok = mid
        return ok + 1
