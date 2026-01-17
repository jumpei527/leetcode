# n = len(bookings)
# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def corpFlightBookings(
        self, bookings: List[List[int]], n: int
    ) -> List[int]:
        num_reserved = [0] * n

        for first, last, seats in bookings:
            num_reserved[first - 1] += seats

            if last < n:
                num_reserved[last] -= seats

        for idx in range(1, n):
            num_reserved[idx] += num_reserved[idx - 1]

        return num_reserved
