class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_char_position = {}
        t_char_position = {}

        for i in range(len(s)):
            if s[i] not in s_char_position:
                s_char_position[s[i]] = i
            if t[i] not in t_char_position:
                t_char_position[t[i]] = i

            if s_char_position[s[i]] != t_char_position[t[i]]:
                return False

        return True
