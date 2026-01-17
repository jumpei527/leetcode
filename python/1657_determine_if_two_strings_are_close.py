# len(word1)
# Time: O(n)
# Space: O(1)


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        word1_dict = {}
        for word in word1:
            word1_dict[word] = word1_dict.get(word, 0) + 1

        word2_dict = {}
        for word in word2:
            word2_dict[word] = word2_dict.get(word, 0) + 1

        return (
            set(word1_dict.keys()) == set(word2_dict.keys()) and
            sorted(word1_dict.values()) == sorted(word2_dict.values())
        )
