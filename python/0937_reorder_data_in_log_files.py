# n = len(logs)
from typing import List


class Solution:
    # Time: O(nlogn)
    # Space: O(n)
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = []
        letter_logs = []

        for log in logs:
            id, words = log.split(maxsplit=1)
            if words[0].isalpha():
                letter_logs += [log]
            else:
                digit_logs += [log]

        letter_logs.sort(
            key=lambda x: (x.split(maxsplit=1)[1], x.split(maxsplit=1)[0])
        )

        return letter_logs + digit_logs


class Solution2:
    # Time: O(nlogn)
    # Space: O(n)
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(logs, key=self.sort)

    def sort(self, logs):
        id, words = logs.split(maxsplit=1)
        if words[0].isalpha():
            return (0, words, id)
        else:
            return (1, None, None)
