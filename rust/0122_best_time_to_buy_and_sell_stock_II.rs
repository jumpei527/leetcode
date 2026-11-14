// n = prices.len()
// Time: O(n)
// Space: O(1)
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut profit = 0;
        let mut buy_price = prices[0];

        for price in prices {
            if price > buy_price {
                profit += price - buy_price;
            }
            buy_price = price;
        }

        profit
    }
}
