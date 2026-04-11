package main

// n = len(nums)
// Time: O(n)
// Space: O(n)
func majorityElement(nums []int) int {
	numToCount := make(map[int]int)
	half := len(nums) / 2

	for _, num := range nums {
		numToCount[num]++
		if numToCount[num] > half {
			return num
		}
	}

	return -1
}
