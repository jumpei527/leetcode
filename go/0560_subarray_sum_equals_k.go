package main

// n = len(nums)
// Time: O(n)
// Space: O(n)
func subarraySum(nums []int, k int) int {
	subarraySum := 0
	prefixSum := 0
	prefixSumCount := make(map[int]int)
	prefixSumCount[0] = 1
	for _, n := range nums {
		prefixSum += n
		if cnt, found := prefixSumCount[prefixSum-k]; found {
			subarraySum += cnt
		}
		prefixSumCount[prefixSum] += 1
	}

	return subarraySum
}
