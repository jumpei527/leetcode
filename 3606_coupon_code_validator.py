# n = len(code)
# Time: O(n log n)
# Space: O(n)
from typing import List


class Solution:
    def validateCoupons(
        self, code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:
        order = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3,
        }
        valid = []
        for code, business, is_active in zip(code, businessLine, isActive):
            if not is_active:
                continue

            if business not in order:
                continue

            if not (
                code and all(char.isalnum() or char == '_' for char in code)
            ):
                continue

            valid.append((order[business], code))

        valid.sort(key=lambda x: (x[0], x[1]))

        return [code for _, code in valid]
