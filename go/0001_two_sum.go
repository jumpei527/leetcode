package main

// n = len(nums)
// Time:  O(n)
// Space: O(n)
func twoSum(nums []int, target int) []int {
	numToIndex := make(map[int]int)

	for i, n := range nums {
		if j, ok := numToIndex[target-n]; ok {
			return []int{j, i}
		}
		numToIndex[n] = i
	}

	return nil
}
