# n = len(s)
# Time: O(n)
# Space: O(1)


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "i", "u", "e", "o", "A", "I", "U", "E", "O"}

        s = list(s)

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            while left < len(s) and s[left] not in vowels:
                left += 1
            while right >= 0 and s[right] not in vowels:
                right -= 1

        return "".join(s)
