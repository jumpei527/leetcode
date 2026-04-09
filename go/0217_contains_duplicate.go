package main

// n = len(nums)
// Time: O(n)
// Space: O(n)
func containsDuplicate(nums []int) bool {
	seen := make(map[int]struct{})

	for _, num := range nums {
		if _, exist := seen[num]; exist {
			return true
		}

		seen[num] = struct{}{}
	}

	return false
}
