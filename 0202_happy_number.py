# n = len(n)
# Time: O(logn)
# Space: O(1)


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            square_sum = 0
            while n:
                digit = n % 10
                square_sum += digit ** 2
                n = n // 10
            n = square_sum

        return True
