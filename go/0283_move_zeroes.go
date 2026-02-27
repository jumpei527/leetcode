package main

// n = len(nums)
// Time:  O(n)
// Space: O(1)
func moveZeroes(nums []int) {
	insertPos := 0

	for i := 0; i < len(nums); i++ {
		if nums[i] != 0 {
			nums[insertPos] = nums[i]
			insertPos++
		}
	}

	for insertPos < len(nums) {
		nums[insertPos] = 0
		insertPos++
	}
}
