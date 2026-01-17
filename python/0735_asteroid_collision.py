# n = len(asteroids)
# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []

        for size in asteroids:
            while ans and size < 0 and ans[-1] > 0:
                if -size > ans[-1]:
                    ans.pop()
                    continue
                elif -size == ans[-1]:
                    ans.pop()
                break
            else:
                ans.append(size)

        return ans
