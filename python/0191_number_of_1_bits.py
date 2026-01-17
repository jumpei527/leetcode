# Time: O(1)
# Space: O(1)


class Solution:
    def hammingWeight(self, n: int) -> int:
        bits_num = 0
        for i in range(32):
            if (n >> i) & 1:
                bits_num += 1

        return bits_num
