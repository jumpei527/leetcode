# n = len(n)
# Time: O(n)
# Space: O(n)
from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:
        digit_map = defaultdict(int)

        for num in range(1, n+1):
            digit_sum = self.calculate_digit_sum(num)
            digit_map[digit_sum] = digit_map.get(digit_sum, 0) + 1

        group_sizes = list(digit_map.values())

        max_group_size = max(group_sizes)
        count = group_sizes.count(max_group_size)

        return count

    def calculate_digit_sum(self, num: int) -> int:
        digit_sum = 0

        while num:
            digit_sum += num % 10
            num //= 10

        return digit_sum
