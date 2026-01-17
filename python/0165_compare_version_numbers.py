# n = max(len(version1), len(version2))
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        parts_1 = version1.split(".")
        parts_2 = version2.split(".")

        for idx in range(max(len(parts_1), len(parts_2))):
            v1 = int(parts_1[idx]) if idx < len(parts_1) else 0
            v2 = int(parts_2[idx]) if idx < len(parts_2) else 0

            if v1 > v2:
                return 1

            if v1 < v2:
                return -1

        return 0
