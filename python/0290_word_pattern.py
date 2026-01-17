# n = len(pattern)
# Time: O(n)
# Time: O(n)

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False
        if len(set(pattern)) != len(set(words)):
            return False

        pattern_to_word = {}

        for i in range(len(pattern)):
            if pattern[i] not in pattern_to_word:
                pattern_to_word[pattern[i]] = words[i]
            elif pattern_to_word[pattern[i]] != words[i]:
                return False

        return True
