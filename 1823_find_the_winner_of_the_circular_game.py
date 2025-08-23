# Time: O(n*k)
# Space: O(n)
from collections import deque


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = deque()
        for idx in range(1, n+1):
            players.append(idx)

        while len(players) > 1:
            for _ in range(k-1):
                n = players.popleft()
                players.append(n)
            players.popleft()

        return players[0]
