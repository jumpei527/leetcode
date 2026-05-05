package main

// n = len(s)
// Time: O(n)
// Space: O(1)
func lengthOfLastWord(s string) int {
	i := len(s) - 1
	count := 0

	for i >= 0 && s[i] == ' ' {
		i--
	}

	for i >= 0 && s[i] != ' ' {
		count++
		i--
	}

	return count
}
