# n = len(gain)
# Time: O(n)
# Space: O(1)
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_altitude = 0
        cur_altitude = 0

        for n in gain:
            cur_altitude += n
            highest_altitude = max(cur_altitude, highest_altitude)

        return highest_altitude
