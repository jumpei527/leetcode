package main

// n = len(nums)
// Time: O(n)
// Space: O(1)
func missingNumber(nums []int) int {
	total := len(nums)

	for i, num := range nums {
		total += i - num
	}

	return total
}
