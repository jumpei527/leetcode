package main

// n = len(nums)
// Time: O(n)
// Space: O(n)
func containsNearbyDuplicate(nums []int, k int) bool {
	numsIndex := make(map[int]int)

	for cur_idx, num := range nums {
		if prev_idx, exist := numsIndex[num]; exist {
			if cur_idx-prev_idx <= k {
				return true
			}
		}
		numsIndex[num] = cur_idx
	}

	return false
}
