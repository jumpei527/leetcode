package main

// n = len(prices)
// Time: O(n)
// Space: O(1)
func maxProfit(prices []int) int {
	profit := 0

	for i := 0; i < len(prices)-1; i++ {
		if prices[i+1]-prices[i] > 0 {
			profit += prices[i+1] - prices[i]
		}
	}

	return profit
}
