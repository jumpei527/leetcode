package main

// n = len(nums)
// Time: O(n)
// Space: O(1)
func jump(nums []int) int {
	jumpCount := 0
	curReach := 0
	nextReach := 0

	for i := 0; i < len(nums)-1; i++ {
		nextReach = max(i+nums[i], nextReach)

		if i == curReach {
			jumpCount++
			curReach = nextReach
		}
	}

	return jumpCount
}
