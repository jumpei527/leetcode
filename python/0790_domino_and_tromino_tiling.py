class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7

        tile_num = [0] * max(3, n)
        tile_num[0] = 1
        tile_num[1] = 2
        tile_num[2] = 5

        for idx in range(3, n):
            tile_num[idx] = (2 * tile_num[idx-1] + tile_num[idx-3]) % MOD

        return tile_num[n-1]
