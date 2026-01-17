# n = len(set(str(num)))
# Time: O(n)
# Space: O(1)


class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)
        num_set = set(num_str)
        max_num = num
        min_num = num

        for digit in num_set:
            for new_digit in "0123456789":
                if digit == num_str[0] and new_digit == "0":
                    continue
                new_num = int(num_str.replace(digit, new_digit))
                max_num = max(new_num, max_num)
                min_num = min(new_num, min_num)

        return max_num - min_num
