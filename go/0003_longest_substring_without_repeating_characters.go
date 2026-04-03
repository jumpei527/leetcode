package main

// n = len(s)
// Time:  O(n)
// Space: O(n)
func lengthOfLongestSubstring(s string) int {
	left := 0
	maxLength := 0
	charIndex := make(map[byte]int)

	for right := 0; right < len(s); right++ {
		ch := s[right]

		if idx, exists := charIndex[ch]; exists && idx >= left {
			left = idx + 1
		}

		charIndex[ch] = right

		if right-left+1 > maxLength {
			maxLength = right - left + 1
		}
	}

	return maxLength
}
