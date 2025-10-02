class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        char_freq = []

        for char in s:
            if char_freq and char_freq[-1][0] == char:
                char_freq[-1][1] += 1
                if char_freq[-1][1] == k:
                    char_freq.pop()
            else:
                char_freq.append([char, 1])

        removed_str = ""
        for char, freq in char_freq:
            removed_str += char * freq

        return removed_str
