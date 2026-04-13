package main

import "strings"

// n = len(pattern)
// m = len(s)
// Time: O(n+m)
// Space: O(n+m)
func wordPattern(pattern string, s string) bool {
	words := strings.Split(s, " ")

	if len(pattern) != len(words) {
		return false
	}

	p2w := make(map[byte]string)
	w2p := make(map[string]byte)

	for i := 0; i < len(words); i++ {
		p := pattern[i]
		w := words[i]

		if mappedWord, ok := p2w[p]; ok {
			if mappedWord != w {
				return false
			}
		} else {
			p2w[p] = w
		}

		if mappedPattern, ok := w2p[w]; ok {
			if mappedPattern != p {
				return false
			}
		} else {
			w2p[w] = p
		}
	}

	return true
}
