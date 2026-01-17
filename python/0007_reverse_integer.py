# Time: O(n)
# Space: O(1)


class Solution:
    def reverse(self, x: int) -> int:
        reverse_num = 0
        if x < 0:
            reverse_num = int(str(x)[1::][::-1]) * (-1)
        else:
            reverse_num = int(str(x)[::-1])

        if reverse_num > 2 ** 31 - 1 or reverse_num < -2 ** 31:
            return 0

        return reverse_num
