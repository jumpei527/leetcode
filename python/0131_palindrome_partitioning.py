# n = len(s)
# Time: O(n^2)
# Space: O(n)
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.partitions = []
        self.backtrack(0, [], s)
        return self.partitions

    def is_palindrome(self, string: str) -> bool:
        return string == string[::-1]

    def backtrack(self, start: int, cur_partition: List[str], s: str) -> None:
        if start == len(s):
            self.partitions.append(cur_partition[:])
            return

        for end in range(start+1, len(s)+1):
            if self.is_palindrome(s[start:end]):
                cur_partition.append(s[start:end])
                self.backtrack(end, cur_partition, s)
                cur_partition.pop()
