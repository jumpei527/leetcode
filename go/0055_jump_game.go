package main

// n = len(nums)
// Time: O(n)
// Space: O(1)
func canJump(nums []int) bool {
	farthest := 0
	for i := 0; i < len(nums); i++ {
		if i > farthest {
			return false
		}

		farthest = max(i+nums[i], farthest)
	}

	return true
}
