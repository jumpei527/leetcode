# n = len(s1)
# Time: O(n)
# Space: O(n)


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        swap_index = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                swap_index.append(i)

        if len(swap_index) == 2:
            i, j = swap_index[0], swap_index[1]
            return s1[i] == s2[j] and s1[j] == s2[i]

        return False
