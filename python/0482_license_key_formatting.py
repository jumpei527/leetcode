# n = len(s)
# Time: O(n)
# Space: O(n)

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        """
        Reformat a given license key string by grouping characters into
        blocks of length k, separated by dashes, and converting all
        lowercase letters to uppercase.

        Args:
            s (str): The input string that consists of only alphanumeric
            characters and dashes.
            k (int): The length of each block after the first block.

        Returns:
            str: The reformatted license key string.

        Examples:
            >>> Solution().licenseKeyFormatting("5F3Z-2e-9-w", 4)
            '5F3Z-2E9W'
        """
        key_str = s.replace("-", "").upper()
        head_length = len(key_str) % k or k
        if len(key_str) <= head_length:
            return key_str

        head = key_str[:head_length]
        body = key_str[head_length:]
        formatted_body = "-".join(body[i:i+k] for i in range(0, len(body), k))

        return head + "-" + formatted_body
