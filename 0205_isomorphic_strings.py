from returns.result import Failure, Success, Result
from returns.pipeline import is_successful


class Solution:
    def is_isomorphic(self, source: str, target: str) -> Result[bool, str]:
        """
        Given two strings, check if they are isomorphic.
        Two strings are isomorphic if the characters in one string can be
        replaced to get the other string. All occurrences of a character
        must be replaced with another character while preserving the
        order of characters.

        Args:
            source: The first string.
            target: The second string.
        Returns:
            Result[bool, str]: A success result with True if the strings
            are isomorphic, or a failure result with an error message.
        Examples:
            >>> Solution().is_isomorphic("egg", "add")
            Success(True)
            >>> Solution().is_isomorphic("foo", "bar")
            Success(False)
        """
        if not source or not target:
            return Failure("Both strings must be non-empty.")

        if len(source) != len(target):
            return Failure("Strings must be of the same length.")

        source_pos_map = {}
        target_pos_map = {}

        for idx in range(len(source)):
            # Remember the first occurrence of each character
            if source[idx] not in source_pos_map:
                source_pos_map[source[idx]] = idx
            if target[idx] not in target_pos_map:
                target_pos_map[target[idx]] = idx

            # Check if the first occurrence positions match
            # If not, the mapping between source and target is not isomorphic
            if source_pos_map[source[idx]] != target_pos_map[target[idx]]:
                return Success(False)

        return Success(True)


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_is_isomorphic_success(self):
        result = self.solution.is_isomorphic("egg", "add")
        assert is_successful(result)
        assert result.unwrap() is True

    def test_is_isomorphic_failure(self):
        result = self.solution.is_isomorphic("foo", "bar")
        assert is_successful(result)
        assert result.unwrap() is False

    def test_is_isomorphic_empty(self):
        result = self.solution.is_isomorphic("", "")
        assert not is_successful(result)
        assert "Both strings must be non-empty." in result.failure()

    def test_is_isomorphic_different_length(self):
        result = self.solution.is_isomorphic("abc", "ab")
        assert not is_successful(result)
        assert "Strings must be of the same length." in result.failure()
