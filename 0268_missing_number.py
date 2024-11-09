from typing import List


class Solution:
    # Time: O(nlogn)
    # Space: O(1)
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i, n in enumerate(nums):
            if i != n:
                return i
        return len(nums)


class Solution2:
    # Time: O(n)
    # Space: O(1)
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums) * (len(nums)+1) // 2
        for n in nums:
            res -= n
        return res


class Solution3:
    # Time: O(nlogn)
    # Space: O(1)
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        ok = -1
        ng = len(nums)
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if mid == nums[mid]:
                ok = mid
            else:
                ng = mid
        return ng
