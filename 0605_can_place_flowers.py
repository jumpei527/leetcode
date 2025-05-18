# n = len(flowerbed)
# Time: O(n)
# Space: O(1)
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        planted_space = 0

        for idx in range(len(flowerbed)):
            if flowerbed[idx] == 0:
                is_left_empty = (
                    idx == 0 or flowerbed[idx-1] == 0
                )
                is_right_empty = (
                    idx == len(flowerbed)-1 or flowerbed[idx+1] == 0
                )
                if is_left_empty and is_right_empty:
                    flowerbed[idx] = 1
                    planted_space += 1

        return planted_space >= n
