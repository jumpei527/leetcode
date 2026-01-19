package main

// n = len(nums1), m = len(nums2)
// Time:  O(n + m)
// Space: O(n)
func intersection(nums1 []int, nums2 []int) []int {
	intersections := []int{}
	seen := make(map[int]bool)

	for _, n := range nums1 {
		seen[n] = true
	}

	for _, n := range nums2 {
		if seen[n] {
			intersections = append(intersections, n)
			delete(seen, n)
		}
	}

	return intersections
}
