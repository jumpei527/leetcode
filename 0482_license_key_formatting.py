# n = len(s)
# Time: O(n)
# Space: O(n)

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        key_str = s.replace("-", "").upper()
        head_length = len(key_str) % k or k
        if len(key_str) <= head_length:
            return key_str

        head = key_str[:head_length]
        body = key_str[head_length:]
        formatted_body = "-".join(body[i:i+k] for i in range(0, len(body), k))

        return head + "-" + formatted_body
