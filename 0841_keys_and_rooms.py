# n: rooms_number
# e: keys_number
# Time: O(n + e)
# Space: O(n)
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = [0]
        visited_rooms = set()

        while keys:
            room = keys.pop()
            visited_rooms.add(room)
            for key in rooms[room]:
                if key not in visited_rooms:
                    keys.append(key)

        return len(visited_rooms) == len(rooms)
