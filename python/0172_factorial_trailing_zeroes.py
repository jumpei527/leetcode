# Time: O(logn)
# Space: O(1)


class Solution:
    def trailingZeroes(self, n: int) -> int:
        zero_cnt = 0
        while n > 0:
            n //= 5
            zero_cnt += n
        return zero_cnt
