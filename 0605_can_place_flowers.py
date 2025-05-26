# n = len(flowerbed)
# Time: O(n)
# Space: O(1)
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Given an integer array flowerbed representing a flowerbed (0 = empty, 1 = planted),
        and an integer n, return true if n new flowers can be planted in the flowerbed
        without violating the no-adjacent-flowers rule.
        
        Args:
            flowerbed (List[int]): The flowerbed represented as a list of integers.
            n (int): The number of new flowers to be planted.
        
        Returns:
            bool: True if n new flowers can be planted, False otherwise.
        
        Examples:
            >>> flowerbed = [1, 0, 0, 0, 1]
            >>> n = 1
            >>> Solution().canPlaceFlowers(flowerbed, n)
            True
            
            >>> flowerbed = [1, 0, 0, 0, 1]
            >>> n = 2
            >>> Solution().canPlaceFlowers(flowerbed, n)
            False
        """
        planted_count = 0

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
                    planted_count += 1

        return planted_count >= n
