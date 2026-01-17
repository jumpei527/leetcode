# m = len(logs)
# Time: O(m)
# Space: O(max(n, m))
from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        exclusive_time = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fid_str, typ, time_str = log.split(":")
            fid = int(fid_str)
            time = int(time_str)

            if typ == "start":
                if stack:
                    exclusive_time[stack[-1]] += time - prev_time
                prev_time = time
                stack.append(fid)
            elif typ == "end":
                exclusive_time[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        return exclusive_time
