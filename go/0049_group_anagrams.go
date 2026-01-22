package main

import "slices"

// n = len(strs)
// m = length of the longest string
// Time: O(n * mlogm)
// Space: O(n * m)
func groupAnagrams(strs []string) [][]string {
	anagramMap := make(map[string][]string)
	for _, s := range strs {
		bytes := []byte(s)
		slices.Sort(bytes)
		key := string(bytes)
		anagramMap[key] = append(anagramMap[key], s)
	}

	result := [][]string{}
	for _, v := range anagramMap {
		result = append(result, v)
	}

	return result
}
