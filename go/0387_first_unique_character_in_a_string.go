package main

// n = len(s)
// Time:  O(n)
// Space: O(n)
func firstUniqChar(s string) int {
	freq := make(map[rune]int)
	for _, char := range s {
		freq[char]++
	}

	for idx, char := range s {
		if freq[char] == 1 {
			return idx
		}
	}

	return -1
}
