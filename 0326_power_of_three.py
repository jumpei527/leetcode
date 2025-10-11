# Time: O(logn)
# Space: O(1)


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % 3 == 0 and n > 0:
            n //= 3

        return n == 1
