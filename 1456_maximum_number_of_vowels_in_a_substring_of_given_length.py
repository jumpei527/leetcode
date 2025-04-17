# n = len(s)
# Time: O(n)
# Space: O(1)


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        cur_vowel_num = 0
        vowel = "aiueo"

        for idx in range(k):
            if s[idx] in vowel:
                cur_vowel_num += 1
        max_vowel_num = cur_vowel_num

        for right in range(k, len(s)):
            if s[left] in vowel:
                cur_vowel_num -= 1
            left += 1
            if s[right] in vowel:
                cur_vowel_num += 1
            max_vowel_num = max(max_vowel_num, cur_vowel_num)

        return max_vowel_num
