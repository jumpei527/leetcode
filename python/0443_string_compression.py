# n = len(chars)
# Time: O(n)
# Space: O(1)
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0

        while read < len(chars):
            cur_length = 1
            while read+1 < len(chars) and chars[read] == chars[read+1]:
                read += 1
                cur_length += 1
            chars[write] = chars[read]
            write += 1
            if cur_length > 1:
                for s in str(cur_length):
                    chars[write] = s
                    write += 1
            read += 1

        return write
