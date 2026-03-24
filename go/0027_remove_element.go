package main

// n = len(nums)
// Time:  O(n)
// Space: O(1)
func removeElement(nums []int, val int) int {
	writeIndex := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] != val {
			nums[writeIndex] = nums[i]
			writeIndex++
		}
	}
	return writeIndex
}
